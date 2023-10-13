# -*- coding: utf-8 -*-

from odoo import models, fields, api


class GoalNote(models.TransientModel):
    _name = 'goal.note.wizard'
    _description = """Wizard to create a new note"""

    author_id = fields.Many2one('hr.employee')
    date = fields.Date(default=fields.Date.today())
    goal_ids = fields.Many2many('goal')
    note = fields.Text()

    note_template = fields.Many2one('goal.note.template', string='Note template')

    def add_note(self, valid=False):
        for wiz in self:
            for goal_id in wiz.goal_ids:
                note_id = self.env['goal.note'].create({
                    'author_id': self.author_id.id,
                    'note': self.note,
                    'goal_id': goal_id.id,
                    'valid_goal': valid
                })

    def valid_goal(self):
        self.add_note(valid=True)

    @api.onchange('note_template')
    def update_note_from_template(self):
        self.note = self.note_template.name
