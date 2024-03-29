# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Formation(models.Model):
    _name = 'formation'
    _description = 'Formation that trainer will teach to trainee'

    tag_ids = fields.Many2many('formation.tag')
