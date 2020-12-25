# -*- coding: utf-8 -*-

from odoo import http


'''
    <link href="/module_name/static/src/css/banner.css"
                        rel="stylesheet">

    @http.route('/testsocial/testsocial', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/testsocial/testsocial/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('testsocial.listing', {
            'root': '/testsocial/testsocial',
            'objects': http.request.env['testsocial.testsocial'].search([]),
        })

    @http.route('/testsocial/testsocial/objects/<model("testsocial.testsocial"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('testsocial.object', {
            'object': obj
        })
'''