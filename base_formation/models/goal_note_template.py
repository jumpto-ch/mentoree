# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GoalNoteTemplate(models.Model):
    _name = 'goal.note.template'
    _description = """Template for writing quickly a typical note"""

    name = fields.Text()
