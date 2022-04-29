# -*- coding: utf-8 -*-

from odoo import models, fields

class SettedGoalEditWizard(models.TransientModel):
    _name = 'setted.goal.edit.wizard'
    _description = "Wizard to change list of subject of a trainee"

    trainee_ids = fields.Many2many('res.partner', 'trainee_rel_editor', 'editor', 'partner', string='trainee')
    subject_ids = fields.Many2many('formation.subject', 'subject_rel_editor', 'editor', 'subject', string='Subject')

    def validate_setted_goal_edition(self):
        for trainee in self.trainee_ids:
            for subject in self.subject_ids:
                self.env['setted.goal'].create({
                    'name': subject.name,
                    'subject_id': subject.id,
                    'trainee_id': trainee.id
                })


