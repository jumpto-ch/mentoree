# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class GoalNote(models.Model):
    _name = 'goal.note'
    _description = """Note added to a goal to comment and/or validate"""

    author_id = fields.Many2one('hr.employee')
    date = fields.Date(default=fields.Date.today())
    goal_id = fields.Many2one('goal')
    valid_goal = fields.Boolean()
    note = fields.Text()

    @api.constrains('valid_goal')
    def _only_one_note_valid_goal(self):
        for note in self:
            if self.search_count([('goal_id', '=', note.goal_id.id),
                                  ('valid_goal', '=', True)]) > 1:
                raise models.ValidationError(_('Only one note can valid the goal'))

