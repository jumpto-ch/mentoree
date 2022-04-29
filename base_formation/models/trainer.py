# -*- coding: utf-8 -*-

from odoo import models, fields


class Mentor(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    _description = 'Mentor information'

    mentoree_ids = fields.One2many('res.users', 'user_id')
