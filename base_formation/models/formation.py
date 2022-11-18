# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Formation(models.Model):
    _name = 'formation'
    _description = """Formation that trainer will teach to trainee"""

    name = fields.Char()
    description = fields.Html()

    subject_ids = fields.Many2many('subject')

    parent_ids = fields.Many2many('formation', 'formation_tree_rel', 'parent', 'child', string='List of parents')
    child_ids = fields.Many2many('formation', 'formation_tree_rel', 'child', 'parent', string='List of childs')
