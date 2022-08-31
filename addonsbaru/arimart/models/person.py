from odoo import api, fields, models


class person(models.Model):
    _name = 'arimart.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')

class kasir(models.Model):
    _name = 'arimart.kasir'
    _inherit = 'arimart.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')

class cleaningservice(models.Model):
    _name = 'arimart.cleaningservice'
    _inherit = 'arimart.person'
    _description = 'New Description'

    id_cln = fields.Char(string='ID Cleaning Service')


    
    
