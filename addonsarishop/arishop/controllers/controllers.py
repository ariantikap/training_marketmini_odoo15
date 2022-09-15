from odoo import http, models, fields
from odoo.http import request
import json

class arishop(http.Controller):
    @http.route('/arishop/getproduk', auth='public', methods=['GET'])
    def getproduk(self, **kw):
        produk = request.env['arishop.produk'].search([])
        isi = []
        for prd in produk:
            isi.append({
                'nama_produk' : prd.name,
                'harga_jual' : prd.harga_jual,
                'stok' : prd.stok 
            })
        return json.dumps(isi)
    
    @http.route('/arishop/getsupplier', auth='public', methods=['GET'])
    def getsupplier(self, **kw):
        supplier = request.env['arishop.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_supplier' : s.name,
                'alamat' : s.alamat,
                'no_telepon' : s.no_telp,
                'produk' : s.produk_id[0].name
            })
        return json.dumps(sup)