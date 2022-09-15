from odoo import api, fields, models


class supplier(models.Model):
    _name = 'arishop.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Supplier')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No Telepon')

    produk_id = fields.Many2many(comodel_name='arishop.produk', 
                                 string='Produk')
    
    
    
