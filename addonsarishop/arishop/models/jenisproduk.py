from odoo import api, fields, models


class jenisproduk(models.Model):
    _name = 'arishop.jenisproduk'
    _description = 'New Description'

    # SELECTION fields
    name = fields.Selection([
        ('sayurloc', 'Sayuran Local'), 
        ('sayurimp', 'Sayuran Impor'), 
        ('buahloc', 'Buah Local'),
        ('buahimp', 'Buah Impor'),
    ], string='Nama Jenis Produk')

    kode_jenis = fields.Char(string='Kode Jenis Produk')
    kode_rak = fields.Char(string='Kode Rak')

    # hitung isi yang ada didalam fields
    jml_produk = fields.Char(compute='_compute_jml_produk', string='Jumlah Produk')
    daftar = fields.Char(string='Daftar produk')
    

    # relasi antar produk dan jenis produk
    produk_ids = fields.One2many(comodel_name='arishop.produk', 
                                 inverse_name='jenisproduk_id', 
                                 string='Daftar Produk')
    
    # fields terisi otomatis
    @api.onchange('name')
    def onchange_kode_jenis(self):
        if (self.name == 'sayurloc'):
            self.kode_jenis = 'say01'
        elif (self.name == 'sayurimp'):
            self.kode_jenis = 'say02' 
        elif (self.name == 'buahloc'):
            self.kode_jenis = 'bu01' 
        elif (self.name == 'buahimp'):
            self.kode_jenis = 'bu02' 
    
    @api.onchange('name')
    def onchange_kode_rak(self):
        if (self.name == 'sayurloc'):
            self.kode_rak = '1 kiri depan'
        elif (self.name == 'sayurimp'):
            self.kode_rak = '1 kiri belakang' 
        elif (self.name == 'buahloc'):
            self.kode_rak = '2 kiri depan' 
        elif (self.name == 'buahimp'):
            self.kode_rak = '2 kiri belakang'
        
    
    # hitung isi fields
    @api.depends('produk_ids')
    def _compute_jml_produk(self):
        for rec in self:
            a = self.env['arishop.produk'].search([('jenisproduk_id', '=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_produk = b
            rec.daftar = a

    

    

    


    
    
