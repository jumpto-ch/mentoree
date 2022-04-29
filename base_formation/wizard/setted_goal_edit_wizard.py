# -*- coding: utf-8 -*-

from odoo import models, fields

class MentoreeSubjectEditWizard(models.TransientModel):
    _name = 'mentoree.subject.edit.wizard'
    _description = "Wizard to change list of subject of a mentoree"

    mentoree_ids = fields.Many2many('res.partner', 'mentoree_rel_editor', 'editor', 'partner', string='Mentoree')
    formation_subject_ids = fields.Many2many('formation.subject', 'formation_subject_rel_editor', 'editor', 'formation_subject', string='Formation\'subject')

    def validate_mentoree_subject_edition(self):
        for m in self.mentoree_ids:
            for fsbj in self.formation_subject_ids:
                self.env['mentoree.subject'].create({
                    'name': fsbj.name,
                    'formation_subject_id': fsbj.id,
                    'mentoree_id': m.id
                })


