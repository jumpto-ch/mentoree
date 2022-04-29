# -*- coding: utf-8 -*-

{
    'name': "Track and validate",

    'summary': """
        This modules aim to define formations and subjects of formation that mentoree have to learn.
        Subject have to be validate by mentor for formation to be complete """,

    'author': "JumpTo",
    'website': "http://jumpto.ch",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'School',
    'version': '13.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'family_base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'data/ir_action_server.xml',
        'data/base.xml',
        'views/setted_goal_views.xml',
        'views/setted_goal_note_views.xml',
        'views/formation_base_views.xml',
        'views/res_partner_views.xml',
        'wizard/setted_goal_edit_wizard_views.xml',
        'wizard/setted_goal_note_wizard_views.xml',
        'views/menu.xml',
    ],
}
