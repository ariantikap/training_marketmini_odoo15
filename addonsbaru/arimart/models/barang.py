from odoo import api, fields, models


class barang(models.Model):
    _name = 'arimart.barang'
    _description = 'New Description'

    name = fields.Char(string='Nama Barang')
    harga_beli = fields.Integer(string='Harga Modal',required=True)
    harga_jual = fields.Integer(string='Harga Jual',required=True)

    # Membuat hubungan, kelompokbarang_id = foreign key, m2one ke kelompokbarang.py
    kelompokbarang_id = fields.Many2one(comodel_name='arimart.kelompokbarang', 
                                        string='Kelompok Barang')
    
    
    
