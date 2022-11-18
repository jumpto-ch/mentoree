# -*- coding: utf-8 -*-

from odoo import models, fields


class Trainee(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = """Trainee information"""

    is_trainee = fields.Boolean('Trainee')
    goal_ids = fields.One2many('goal', 'trainee_id', ondelete='cascade')
    count_total_goals = fields.Integer('Number of goal to validate', compute="_compute_count_total_goals")
    trainer_id = fields.Many2one('hr.employee')

    def _compute_count_total_goals(self):
        for r in self:
            r.count_total_goals = len(r.goal_ids)

    def add_subject(self, added_subjects):
        for trainee in self.filtered('is_trainee'):
            for subject in added_subjects:
                trainee.env['goal'].create({
                    'trainee_id': trainee.id,
                    'subject_id': subject.id
                })

    def update_goals(self):
        all_subject = self.env['subject'].search([])

        for trainee in self.filtered('is_trainee'):
            missing_subject = all_subject - trainee.goal_ids.mapped('subject_id') if trainee.goal_ids else all_subject
            trainee.add_subject(missing_subject)

    def action_goal_edit(self):
        view_id = self.env.ref('base_formation.goal_edit_wizard_form').id
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [(view_id, 'form')],
            'res_model': 'goal.edit.wizard',
            'view_id': view_id,
            'target': 'new',
        }
