# -*- coding: utf-8 -*-

from odoo import models, fields


class PerStudent(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Mentoree information'

    is_mentoree = fields.Boolean('Mentoree')
    mentoree_subject_ids = fields.One2many('mentoree.subject', 'mentoree_id', ondelete='cascade')
    count_total_subject = fields.Integer('Number of subject to achieve', compute="_compute_count_total_subjects")
    mentor_id = fields.Many2one('hr.employee')

    def _compute_count_total_subjects(self):
        for r in self:
            r.count_total_subjects = len(r.mentoree_subject_ids)

    def add_subject(self, add_fsbj):
        for mentoree in self.filtered('is_mentoree'):
            for fsbj in add_fsbj:
                mentoree.env['mentoree.subject'].create({
                    'mentoree_id': mentoree.id,
                    'formation_subject_id': fsbj.id
                })

    def update_goals(self):
        all_fsbj = self.env['formation.subject'].search([])

        for mentoree in self.filtered('is_mentoree'):
           missing_fsbj = all_fsbj - mentoree.mentoree_subject_ids.mapped('formation_subject_id') if mentoree.mentoree_subject_ids else all_fsbj
           mentoree.add_subject(missing_fsbj)

    def action_mentoree_subject_edit(self):
        view_id = self.env.ref('trackandvalidate.mentoree_subject_edit_wizard_form').id
        return {
            'name': 'Edit subject attribution',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [(view_id, 'form')],
            'res_model': 'mentoree.subject.edit.wizard',
            'view_id': view_id,
            'target': 'new',
        }