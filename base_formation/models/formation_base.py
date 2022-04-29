# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Subject(models.Model):
    _name = 'formation.subject'
    _description = 'a subject is a achievable part of a formation'

    name = fields.Char()
    description = fields.Html()
    formation_ids = fields.Many2many('formation', 'formation_subject_rel', 'subject', 'formation', string='Formation')

class Formation(models.Model):
    _name = 'formation'
    _description = 'Formation that trainer will teach to trainee'

    name = fields.Char()
    subject_ids = fields.Many2many('formation.subject', 'formation_subject_rel', 'formation', 'subject', string='Subjects')

    parent_ids = fields.Many2many('formation', 'formation_tree_rel', 'parent', 'child', string='List of parents')
    child_ids = fields.Many2many('formation', 'formation_tree_rel', 'child', 'parent', string='List of childs')
