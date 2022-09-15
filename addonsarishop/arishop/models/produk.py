from odoo import api, fields, models

class produk(models.Model):
    _name = 'arishop.produk'
    _description = 'New Description'

    name = fields.Char(string='Nama produk')
    stok = fields.Integer(string='Stok')
    harga_jual = fields.Integer(string='Harga jual',required=True)
    harga_beli = fields.Integer(string='Harga beli',required=True)
    # relasi antar produk dan jenis produk
    jenisproduk_id = fields.Many2one(comodel_name='arishop.jenisproduk', 
                                     string='Jenis Produk',
                                     ondelete='cascade')
    # relasi antar produk dan supplier
    supplier_id = fields.Many2many(comodel_name='arishop.supplier', 
                                   string='Supplier')
    # view simbol RP
    currency_id = fields.Many2one('res.currency', string='Mata Uang',
        help="Forces all moves for this account to have this account currency.", required=True)
    
    
    
