# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re

class FormationSubject(models.Model):
    _name = 'formation.subject'
    _description = 'Subject formation'

    name = fields.Char()
    description = fields.Html()
    formation_id = fields.Many2one('formation')

class Formation(models.Model):
    _name = 'formation'
    _description = 'Formation that mentoree will study'

    name = fields.Char()
    description = fields.Char()
    formation_subject_id = fields.One2many('formation.subject',
                                      inverse_name='formation_id', string='Formation\'s subjects')