# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api


class SettedGoal(models.Model):
    _name = 'setted.goal'
    _description = 'subject assign to a trainee'

    name = fields.Char()
    is_achieve = fields.Boolean("Achieve", compute="_compute_is_achieve", store=True)
    trainee_id = fields.Many2one('res.partner')
    achieve_date = fields.Date("Date", default=False)
    notes_ids = fields.One2many('setted.goal.note', inverse_name='setted_goal_id', string='note')
    subject_id = fields.Many2one('formation.subject')

    subject_name = fields.Char(string='Subject name',
                               related='subject_id.name', readonly=True, store=True)
    state = fields.Selection([
        ('to_do', 'To Do'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
    ], default='to_do', compute="_compute_state", inverse='_inverse_state', store=True)

    @api.depends('notes_ids', 'notes_ids.valid_goal')
    def _compute_state(self):
        for setted_goal in self:
            valid_note = setted_goal.notes_ids.filtered(lambda r: r.valid_goal is True)
            if valid_note:
                setted_goal.state = 'done'
                setted_goal.achieve_date = valid_note[0].date
            else:
                setted_goal.state = 'progress'

    def _inverse_state(self):
        for setted_goal in self:
            setted_goal.achieve_date = False

    def invalid_per_goal(self):
        for setted_goal in self:
            setted_goal.notes_ids.valid_goal = False

    def action_add_note(self):
        view_id = self.env.ref('base_formation.setted_goal_note_wizard_view_form').id
        context = self._context.copy()
        context['default_author_id'] = self.env.user.employee_id.id
        context['default_setted_goal_ids'] = self.ids
        return {
            'name': 'Add new note',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [(view_id, 'form')],
            'res_model': 'setted.goal.note.wizard',
            'view_id': view_id,
            'target': 'new',
            'context': context,
        }
