from odoo import api, fields, models

# omodi = model inherit
class konsumen(models.Model):
    _inherit = 'res.partner'
    _description ='konsumen'

    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')
    
    
