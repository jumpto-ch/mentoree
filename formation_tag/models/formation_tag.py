# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import re


class FormationTag(models.Model):
    _name = 'formation.tag'
    _description = 'tag that help filter formation'

    name = fields.Char()
    formation_ids = fields.Many2many('formation')
