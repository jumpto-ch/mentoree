# -*- coding: utf-8 -*-

from odoo import models, fields


class Trainer(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'
    _description = 'Trainer information'

    trainee_ids = fields.One2many('res.users', 'user_id')
