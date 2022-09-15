
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class penjualan(models.Model):
    _name = 'arimart.penjualan'
    _description = 'New Description'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(string='Tgl Transaksi')
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    detailpenjualan_ids = fields.One2many(
        comodel_name='arimart.detailpenjualan', 
        inverse_name='penjualan_id', 
        string='Detail Penjualan')

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['arimart.detailpenjualan'].search([('penjualan_id','=',rec.id)]).mapped('subtotal'))
            rec.total_bayar = a
    
    # @api.ondelete(at_uninstall=False)
    # def _ondelete_penjualan(self):
    #     if self.detailpenjualan_ids:
    #         a = []
    #         for rec in self:
    #             a = self.env['arimart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
    #             print(a)
    #         for ob in a:
    #             print(str(ob.barang_id.name) + ' ' + str(ob.qty))
    #             ob.barang_id.stok += ob.qty
    
    # Metode Unlink untuk menghapus
    # (saran untuk odoo 14, odoo 15 bisa pakai kedua nya ondelete/unlink)
    def unlink(self):
        if self.detailpenjualan_ids:
            a = []
            for rec in self:
                a = self.env['arimart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
                print(a)
            for ob in a:
                print(str(ob.barang_id.name) + ' ' + str(ob.qty))
                ob.barang_id.stok += ob.qty
        record = super(penjualan,self).unlink()

    #  Untuk meng EDIT STOK BARANG, yg di eksekusi ketika klik tombol edit
    def write(self, vals):
        # membalikan barang dulu
        for rec in self:
            a = self.env['arimart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.barang_id.name)+' '+str(data.qty)+' '+str(data.barang_id.stok))
                data.barang_id.stok += data.qty
        record = super(penjualan,self).write(vals)
        # menambah barang / mengedit barang
        for rec in self:
            b = self.env['arimart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.barang_id.name)+' '+str(databaru.qty)+' '+str(databaru.barang_id.stok))
                    databaru.barang_id.stok -= databaru.qty
                else:
                    pass
        return record

    # SQL CONSTRAINS
    _sql_constraints = [
        # ('constraint_uniq_name','sql_code','message'), STRUKTURNYA
        ('no_nota_unik','unique (name)','No Nota gak boleh sama !!!'),
    ]

    
class detailpenjualan(models.Model):
    _name = 'arimart.detailpenjualan'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(comodel_name='arimart.penjualan', string='Detail Penjualan')
    barang_id = fields.Many2one(comodel_name='arimart.barang', string='List Barang')
    
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')
    
    # Subtotal
    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan
    
    # Harga Satuan
    @api.onchange('barang_id')
    def onchange_barang_id(self):
        if (self.barang_id.harga_jual):
            self.harga_satuan = self.barang_id.harga_jual 

    # Metode Create untuk stok barang
    @api.model
    def create(self,vals):
        record = super(detailpenjualan,self).create(vals)
        # akan dieksekusi setelah klik save
        if record.qty:
            self.env['arimart.barang'].search([('id','=',record.barang_id.id)]).write({'stok' : record.barang_id.stok - record.qty})
        return record
        # atau memakai ini
        # if record.qty:
        #     record.barang_id.stok = record.barang_id.stok - record.qty
    
    # Python CONSTRAINTS
    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("Mau beli {} berapa banyak sih ?!".format(rec.barang_id.name))
            elif (rec.barang_id.stok < rec.qty):
                raise ValidationError("Stok {} ga cukup, hanya ada {}".format(rec.barang_id.name,rec.barang_id.stok))



    
    
    

    
    
    
    


