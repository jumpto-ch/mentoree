# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api


class Goal(models.Model):
    _name = 'goal'
    _description = """A goal represent a subject assign to a trainee"""

    name = fields.Char()
    validation_date = fields.Date(default=False)
    notes_ids = fields.One2many('goal.note', inverse_name='goal_id')

    subject_id = fields.Many2one('subject')
    formation_id = fields.Many2one('formation',
                                   related='subject_id.formation_id', readonly=True, store=True)

    subject_name = fields.Char(string='Subject name', related='subject_id.name', readonly=True, store=True)
    formation_name = fields.Char(string='Formation name', related='formation_id.name', readonly=True, store=True)

    state = fields.Selection([
        ('to_do', 'To do'),
        ('progress', 'In progress'),
        ('done', 'Done'),
    ], default='to_do', compute="_compute_state", inverse='_inverse_state', store=True)

    trainee_id = fields.Many2one('res.partner')

    @api.depends('notes_ids', 'notes_ids.valid_goal')
    def _compute_state(self):
        for goal in self:
            valid_note = goal.notes_ids.filtered(lambda r: r.valid_goal is True)
            if valid_note:
                goal.state = 'done'
                goal.validation_date = valid_note[0].date
            else:
                goal.state = 'progress'

    def _inverse_state(self):
        for goal in self:
            goal.validation_date = False

    def invalid_goal(self):
        for goal in self:
            goal.notes_ids.valid_goal = False

    def action_add_note(self):
        view_id = self.env.ref('base_formation.goal_note_wizard_view_form').id
        context = self._context.copy()
        context['default_author_id'] = self.env.user.employee_id.id
        context['default_goal_ids'] = self.ids
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [(view_id, 'form')],
            'res_model': 'goal.note.wizard',
            'view_id': view_id,
            'target': 'new',
            'context': context,
        }
