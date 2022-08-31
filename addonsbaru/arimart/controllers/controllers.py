# -*- coding: utf-8 -*-
# from odoo import http


# class Arimart(http.Controller):
#     @http.route('/arimart/arimart', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arimart/arimart/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('arimart.listing', {
#             'root': '/arimart/arimart',
#             'objects': http.request.env['arimart.arimart'].search([]),
#         })

#     @http.route('/arimart/arimart/objects/<model("arimart.arimart"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arimart.object', {
#             'object': obj
#         })
