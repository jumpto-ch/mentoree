# -*- coding: utf-8 -*-

from odoo import models, fields


class GoalEditWizard(models.TransientModel):
    _name = 'goal.edit.wizard'
    _description = """Wizard to add a list of subject of a trainee"""

    trainee_ids = fields.Many2many('res.partner')
    subject_ids = fields.Many2many('subject')

    def validate_goal_edition(self):
        for trainee in self.trainee_ids:
            for subject in self.subject_ids:
                self.env['goal'].create({
                    'name': subject.name,
                    'subject_id': subject.id,
                    'trainee_id': trainee.id
                })


