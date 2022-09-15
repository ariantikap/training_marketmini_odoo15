from odoo import api, fields, models

class respartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_konsumen = fields.Boolean(string='Is Konsumen')
    id_konsumen = fields.Char(string='Id Konsumen',
                                 required=False,
                                 domain="[('is_konsumen','=', True)]")
    poin = fields.Integer(string='Poin', domain="[('is_konsumen','=', True)]")
    
    
    


