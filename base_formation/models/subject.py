# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Subject(models.Model):
    _name = 'subject'
    _description = 'a subject is a achievable part of a formation'

    name = fields.Char()
    description = fields.Html()

    formation_ids = fields.Many2many('formation')
    formation_id = fields.Many2one('formation', compute='_compute_formation_id')

    formation_name = fields.Char(related='formation_id.name', readonly=True, store=True)

    @api.depends('formation_ids')
    def _compute_formation_id(self):
        for r in self:
            r.formation_id = r.formation_ids[0] if 0 < len(r.formation_ids) else []

