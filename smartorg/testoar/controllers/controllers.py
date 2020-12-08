# -*- coding: utf-8 -*-
# from odoo import http


# class Testoar(http.Controller):
#     @http.route('/testoar/testoar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testoar/testoar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testoar.listing', {
#             'root': '/testoar/testoar',
#             'objects': http.request.env['testoar.testoar'].search([]),
#         })

#     @http.route('/testoar/testoar/objects/<model("testoar.testoar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testoar.object', {
#             'object': obj
#         })
