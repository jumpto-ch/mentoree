# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PerGoalNoteTemplate(models.Model):
    _name = 'mentoree.subject.note.template'
    _description = 'Mentoree\'s subject note template'

    name = fields.Text()
