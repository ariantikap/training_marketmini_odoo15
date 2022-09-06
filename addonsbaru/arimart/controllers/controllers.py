from odoo import http, models, fields
from odoo.http import request
import json

class arimart(http.Controller):
    @http.route('/arimart/getbarang', auth='public', methods=['GET'])
    def getbarang(self, **kw):
        barang = request.env['arimart.barang'].search([])
        isi = []
        for brg in barang:
            isi.append({
                'nama_barang' : brg.name,
                'harga_jual' : brg.harga_jual,
                'stok' : brg.stok 
            })
        return json.dumps(isi)
    
    @http.route('/arimart/getsupplier', auth='public', methods=['GET'])
    def getsupplier(self, **kw):
        supplier = request.env['arimart.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telepon' : s.no_telp,
                'barang' : s.barang_id[0].name
            })
        return json.dumps(sup)