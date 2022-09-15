from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import datetime

class transaksi(models.Model):
    _name = 'arishop.transaksi'
    _description = 'New Description'

    tgl_beli = fields.Datetime(string='Tgl Transaksi')
    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Many2one(comodel_name='res.partner', string='Nama Pembeli')
    id_konsumen = fields.Char(compute="_compute_id_konsumen",
                              string='Id_konsumen',
                              required=False)
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')

    # relasi antar transaksi dan detailjual
    detailjual_ids = fields.One2many(comodel_name='arishop.detailjual', 
                                    inverse_name='transaksi_id', 
                                    string='Detail Transaksi')
    
    # Membuat STATE untuk melacak kondisi suatu record
    state = fields.Selection(string='Status', 
                            selection=[('draft', 'Draft'),
                                       ('confirm', 'Confirm'),
                                       ('done', 'Done'), 
                                       ('cancel', 'Cancelled')
                                        ],
                            required=True, readonly=True, default='draft')
    
    currency_id = fields.Many2one('res.currency', string='Mata Uang', 
        help="Forces all moves for this account to have this account currency.", required=True)

    # function button state
    def action_confirm(self):
        self.write({'state': 'confirm'})
    def action_done(self):
        self.write({'state': 'done'})
    def action_cancel(self):
        self.write({'state': 'cancel'})
    def action_draft(self):
        self.write({'state': 'draft'})


    @api.depends('nama_pembeli')
    def _compute_id_konsumen(self):
        for rec in self:
            rec.id_konsumen = rec.nama_pembeli.id_konsumen

    # Datetime Otomatis
    @api.model
    def default_get(self, fields):
        res = super(transaksi, self).default_get(fields)
        res.update({'tgl_beli': datetime.now()})
        return res
    
    # hitung total bayar
    @api.depends('detailjual_ids')
    def _compute_totalbayar(self):
        for record in self:
            a = sum(self.env['arishop.detailjual']\
                .search([('transaksi_id','=',record.id)])\
                .mapped('subtotal'))
            record.total_bayar = a
    

    # Metode UNLINK untuk DELETE
    def unlink(self):
        for rec in self:
        # hanya state draft yang bisa di hapus
            if self.filtered(lambda line: line.state != 'draft'):
                raise ValidationError("Selain DRAFT, tidak dapat dihapus !!!")
        # action DELETE STOK
            if rec.detailjual_ids:
                for data in rec.detailjual_ids:
                    data.produk_id.stok = data.produk_id.stok + data.qty
        record = super(transaksi,self).unlink()
        return record

        # else:
        #     # action DELETE STOK
        #     if self.detailjual_ids:
        #         a = []
        #         for rec in self:
        #             a = self.env['arishop.detailjual']\
        #             .search([('transaksi_id','=',rec.id)])
        #             print(a)
        #         for objek in a:
        #             print(str(objek.produk_id.name)+' '+str(objek.qty))
        #             objek.produk_id.stok += objek.qty
        #     record = super(transaksi,self).unlink()

    # untuk EDIT STOK ketika sudah berkurang/bertambah
    def write(self, vals):
        for rec in self:
            a = self.env['arishop.detailjual']\
            .search([('transaksi_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.produk_id.name)+' '+str(data.qty)+' '+str(data.produk_id.stok))
                data.produk_id.stok += data.qty
        record = super(transaksi,self).write(vals)
        # input data barunya
        for rec in self:
            b = self.env['arishop.detailjual']\
            .search([('transaksi_id','=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.produk_id.name)+' '+str(databaru.qty)+' '+str(databaru.produk_id.stok))
                    databaru.produk_id.stok -= databaru.qty
                else:
                    pass
        return record


class detailjual(models.Model):
    _name = 'arishop.detailjual'
    _description = 'New Description'

    name = fields.Char(string='Name')

    # relasi
    transaksi_id = fields.Many2one(comodel_name='arishop.transaksi', 
                                  string='Detail Transaksi')
    produk_id = fields.Many2one(comodel_name='arishop.produk', 
                                string='List Produk')
    
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    # hitung subtotal
    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.qty * record.harga_satuan 
    
    # harga satuan
    @api.onchange('produk_id')
    def onchange_produk_id(self):
        if (self.produk_id.harga_jual):
            self.harga_satuan = self.produk_id.harga_jual
    
    # metode create untuk stok produk, eksekusi setelah SAVE
    @api.model
    def create(self, vals):
        record = super(detailjual,self).create(vals)
        if record.qty:
            self.env['arishop.produk'].search([('id','=',record.produk_id.id)])\
            .write({'stok' : record.produk_id.stok - record.qty}) 
        # if record.qty:
        #     record.produk_id.stok = record.produk_id.stok - record.qty       
        return record
    

    # Python CONSTRAINTS - Validasi eror
    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Mau beli {} berapa banyak sih ?!"\
                .format(rec.produk_id.name))
            elif (rec.produk_id.stok < rec.qty):
                raise ValidationError("Stok {} ga cukup, hanya ada {}"\
                .format(rec.produk_id.name,rec.produk_id.stok))

    
    
    
    
    
