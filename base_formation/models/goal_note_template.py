# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GoalNoteTemplate(models.Model):
    _name = 'goal.note.template'
    _description = 'Trainee\'s subject note template'

    name = fields.Text()
