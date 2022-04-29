# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SettedGoalNote(models.Model):
    _name = 'setted.goal.note'
    _description = 'Manage trainee\'s subject note'

    author_id = fields.Many2one('hr.employee')
    date = fields.Date(default=fields.Date.today())
    setted_goal_id = fields.Many2one('setted.goal')
    valid_goal = fields.Boolean()
    note = fields.Text()

    @api.constrains('valid_goal')
    def _only_one_note_valid_goal(self):
        for note in self:
            if self.search_count([('setted_goal_id', '=', note.setted_goal_id.id),
                                  ('valid_goal', '=', True)]) > 1:
                raise models.ValidationError('Only one note can valid the goal')

