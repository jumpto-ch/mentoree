# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PerGoalNote(models.Model):
    _name = 'mentoree.subject.note'
    _description = 'Manage mentoree\'s subject note'

    author_id = fields.Many2one('hr.employee')
    date = fields.Date(default=fields.Date.today())
    mentoree_subject_id = fields.Many2one('mentoree.subject')
    valid_goal = fields.Boolean()
    note = fields.Text()

    @api.constrains('valid_goal')
    def _only_one_note_valid_goal(self):
        for note in self:
            if self.search_count([('mentoree_subject_id', '=', note.mentoree_subject_id.id),
                                  ('valid_goal', '=', True)]) > 1:
                raise models.ValidationError('Only one note can valid the goal')

