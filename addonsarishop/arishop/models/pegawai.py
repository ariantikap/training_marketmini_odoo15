from odoo import api, fields, models


class pegawai(models.Model):
    _name = 'arishop.pegawai'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    tgl_awalkerja = fields.Date(string='Tgl Awal Masuk Keja')

class kasir(models.Model):
    _name = 'arishop.kasir'
    _inherit = 'arishop.pegawai'
    _description = 'New Description'

    id_kasir = fields.Char(string='ID Kasir')

class pelayan(models.Model):
    _name = 'arishop.pelayan'
    _inherit = 'arishop.pegawai'
    _description = 'New Description'

    id_plyn = fields.Char(string='ID Pelayan')

class supervisor(models.Model):
    _name = 'arishop.supervisor'
    _inherit = 'arishop.pegawai'
    _description = 'New Description'

    id_svisor = fields.Char(string='ID Supervisor')

    