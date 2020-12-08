# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'testoar.wizard'
    _description = "Wizard: Quick Registration of Attendees to Sessions"

    def _default_session(self):
        return self.env['testoar.session'].browse(self._context.get('active_id'))

    session_id = fields.Many2one('testoar.session',
        string="Session", required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    def subscribe(self):
        for session in self.session_id:
            session.attendee_ids |= self.attendee_ids
            # self.session_id.attendee_ids |= self.attendee_ids
        return {}