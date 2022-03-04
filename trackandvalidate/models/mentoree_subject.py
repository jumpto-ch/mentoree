# -*- coding: utf-8 -*-
import re
from odoo import models, fields, api


class PerGoal(models.Model):
    _name = 'mentoree.subject'
    _description = 'subject assign to a mentoree'

    name = fields.Char()
    is_achieve = fields.Boolean("Achieve", compute="_compute_is_achieve", store=True)
    mentoree_id = fields.Many2one('res.partner')
    achieve_date = fields.Date("Date", default=False)
    notes_ids = fields.One2many('mentoree.subject.note', 'mentoree.subject', string='note')
    formation_subject_id = fields.Many2one('formation.subject')

    formation_id = fields.Many2one(related='formation_subject_id.formation_id', store=True)
    formation_subject_description = fields.Char(string='formation\'s subject description',
                                                related='formation_subject_id.name', readonly=True, store=True)
    formation_description = fields.Char(string='formation\'s description',
                                        related='formation_id.description', readonly=True, store=True)
    state = fields.Selection([
        ('to_do', 'To Do'),
        ('progress', 'In Progress'),
        ('done', 'Done'),
    ], default='to_do', compute="_compute_state", inverse='_inverse_state', store=True)

    @api.depends('notes_ids', 'notes_ids.valid_goal')
    def _compute_state(self):
        for msbj in self:
            valid_note = msbj.notes_ids.filtered(lambda r: r.valid_goal is True)
            if valid_note:
                msbj.state = 'done'
                msbj.achieve_date = valid_note[0].date
            else:
                msbj.state = 'progress'

    def _inverse_state(self):
        for msbj in self:
            msbj.achieve_date = False

    def invalid_per_goal(self):
        for msbj in self:
            msbj.notes_ids.valid_goal = False

    def action_add_note(self):
        view_id = self.env.ref('trackandvalidate.mentoree_subject_note_wizard_view_form').id
        context = self._context.copy()
        context['default_author_id'] = self.env.user.employee_id.id
        context['default_mentoree_subject_ids'] = self.ids
        return {
            'name': 'Add new note',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [(view_id, 'form')],
            'res_model': 'mentoree.subject.note.wizard',
            'view_id': view_id,
            'target': 'new',
            'context': context,
        }
