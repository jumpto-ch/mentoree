# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SettedGoalNoteTemplate(models.Model):
    _name = 'setted.goal.note.template'
    _description = 'Trainee\'s subject note template'

    name = fields.Text()
