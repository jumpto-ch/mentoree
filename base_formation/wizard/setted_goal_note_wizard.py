# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SettedGoalNote(models.TransientModel):
    _name = 'setted.goal.note.wizard'
    _description = "Wizard to add note"

    author_id = fields.Many2one('hr.employee')
    date = fields.Date(default=fields.Date.today())
    setted_goal_ids = fields.Many2many('setted.goal', String="Setted goal")
    note = fields.Text()

    note_template = fields.Many2one('setted.goal.note.template')

    def add_note(self, valid=False):
        for wiz in self:
            for setted_goal_id in wiz.setted_goal_ids:
                note_id = self.env['setted.goal.note'].create({
                    'author_id': self.author_id.id,
                    'note': self.note,
                    'setted_goal_id': setted_goal_id.id,
                    'valid_goal': valid
                })

    def valid_goal(self):
        self.add_note(valid=True)

    @api.onchange('note_template')
    def update_note_from_template(self):
        self.note = self.note_template.name
