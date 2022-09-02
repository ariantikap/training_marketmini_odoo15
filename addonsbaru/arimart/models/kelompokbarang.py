from odoo import api, fields, models


class kelompokbarang(models.Model):
    _name = 'arimart.kelompokbarang'
    _description = 'New Description'

    # Membuat SELECTION FIELDS (dropdown fields)
    name = fields.Selection([
        ('makananbasah', 'Makanan Basah'), 
        ('makanankering', 'Makanan Kering'), 
        ('minuman', 'Minuman'), 
    ], string='Nama Kelompok')

    # Membuat COMPUTED FIELDS (sudah mengisi secara otomatis)
    # kode_kelompok = fields.Char(onchange='_compute_kode_kelompok', string='Kode Kelompok')
    kode_kelompok = fields.Char(string='Kode Kelompok')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if (self.name == 'makananbasah'):
            self.kode_kelompok = 'mak01'
        elif (self.name == 'makanankering'):
            self.kode_kelompok = 'mak02'
        elif (self.name == 'minuman'):
            self.kode_kelompok = 'min'

    kode_rak = fields.Char(string='Kode Rak')

    # Membuat hubungan o2m ke barang.py. barang_ids = foreign key
    # pake "s" karena isi dari barang itu banyak 

    barang_ids = fields.One2many(comodel_name='arimart.barang', 
                                inverse_name='kelompokbarang_id', 
                                string='Daftar Barang')
    # hitung isi fields
    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')
    
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['arimart.barang'].search([('kelompokbarang_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a
    
    daftar = fields.Char(string='Daftar Isi')
    
    
