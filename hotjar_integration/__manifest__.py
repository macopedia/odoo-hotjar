# -*- coding: utf-8 -*-
{
    'name': "Odoo-Hotjar Integration",

    'summary': """
         This module adds the possibility to connect your Odoo-generated website with Hotjar. 
        This will enable even better tracking of user behavior on your company's website.
        All you need to do is to mark 'Hotjar active' and then fill 'Hotjar site ID' field in website form with ID generated on Hotjar side.
        """,
    'author': "Macopedia",
    'website': "https://macopedia.com/",
    "license": "AGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'views/website.xml',
        'views/website_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
}
