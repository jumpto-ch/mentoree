# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MentoreeSubjectNote(models.TransientModel):
    _name = 'mentoree.subject.note.wizard'
    _description = "Wizard to add note"

    author_id = fields.Many2one('hr.employee')
    date = fields.Date(default=fields.Date.today())
    mentoree_subject_ids = fields.Many2many('mentoree.subject', String="Subject")
    note = fields.Text()

    note_template = fields.Many2one('mentoree.subject.note.template')

    def add_note(self, valid=False):
        for wiz in self:
            for msbj_id in wiz.mentoree_subject_ids:
                note_id = self.env['mentoree.subject.note'].create({
                    'author_id': self.author_id.id,
                    'note': self.note,
                    'mentoree_subject_id': msbj_id.id,
                    'valid_goal': valid
                })

    def valid_goal(self):
        self.add_note(valid=True)

    @api.onchange('note_template')
    def update_note_from_template(self):
        self.note = self.note_template.name
