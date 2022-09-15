from odoo import fields, models, api

class transaksireport(models.TransientModel):
    _name = 'arishop.transaksireport'
    _description = 'Description'

    konsumen_id = fields.Many2one(comodel_name='res.partner', 
                                  string='Konsumen',
                                  required=False)
    dari_tgl = fields.Date(string='Dari tanggal',
                            required=False)
    ke_tgl = fields.Date(string='Ke tanggal',
                         required=False)

    def button_transaksi_report(self):
        filter = []
        konsumen_id = self.konsumen_id
        dari_tgl = self.dari_tgl
        ke_tgl = self.ke_tgl
        if konsumen_id:
            filter += [('nama_pembeli', '=', konsumen_id.id)]
        if dari_tgl:
            filter += [('tgl_beli', '>=', dari_tgl)]
        if ke_tgl:
            filter += [('tgl_beli', '<=', ke_tgl)]
        print(filter)
        transaksi = self.env['arishop.transaksi'].search_read(filter)
        print(transaksi)
        data = {
            'form': self.read()[0],
            'transaksixx': transaksi,
        }
        print(data)
        return self.env.ref('arishop.wizard_transaksireport_pdf').report_action(self, data=data)
    
    

    

    

