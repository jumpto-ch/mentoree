# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re

class FormationTag(models.Model):
    _name = 'formation.tag'
    _description = 'tag that help filter formation'

    name = fields.Char()
    formation_ids = fields.Many2many('formation', 'formation_tag_rel', 'tag', 'formation', string='Formation')

class FormationSubject(models.Model):
    _name = 'formation.subject'
    _description = 'Subject formation'

    name = fields.Char()
    description = fields.Html()
    formation_ids = fields.Many2many('formation', 'formation_subject_rel', 'subject', 'formation', string='Formation')

class Formation(models.Model):
    _name = 'formation'
    _description = 'Formation that mentoree will study'

    name = fields.Char()
    formation_subject_ids = fields.Many2many('formation.subject', 'formation_subject_rel', 'formation', 'subject', string='Formation\'s subjects')

    formation_parent_ids = fields.Many2many('formation', 'formation_tree_rel', 'parent', 'child', string='List of parents')
    formation_child_ids = fields.Many2many('formation', 'formation_tree_rel', 'child', 'parent', string='List of childs')

    formation_tag_ids = fields.Many2many('formation.tag', 'formation_tag_rel', 'formation', 'tag', string='Tag')

