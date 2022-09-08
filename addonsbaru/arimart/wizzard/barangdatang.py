from odoo import api, fields, models


class barangdatang(models.TransientModel):
    _name = 'arimart.barangdatang'

    barang_id = fields.Many2one(
        comodel_name='arimart.barang', 
        string='Nama Barang',
        required=True)

    jumlah = fields.Integer(
        string='Jumlah',
        required=False)

    def button_barang_datang(self):
        for rec in self:
            self.env['arimart.barang']\
            .search([('id','=',rec.barang_id.id)])\
            .write({'stok': rec.barang_id.stok + rec.jumlah})
     
    

