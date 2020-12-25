
from odoo import models, fields, api
from ..models import worksheet
from ..models.worksheet import Requirement
from odoo import http


class testsocial(http.Controller):
    @http.route('/testsocial/hello/', auth='public')
    def hello(self,**kw):
        return http.request.render('testsocial.index', {
            'teachers': ["Thinker CHN", "Jody Caroll", "Lester Vaughn"],
        })

    @http.route('/testsocial/host/', auth='public')
    def HostReqirement(self,**kw):
        Objs = http.request.env['testsocial.requirement']

        

        return http.request.render('testsocial.indexx', {
            'objs': Objs.search([])
        })
