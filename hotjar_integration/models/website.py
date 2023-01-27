# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Model(models.Model):
    _inherit = "website"

    hotjar_active = fields.Boolean("Is Hotjar integration active?", default=False)

    hotjar_site_id = fields.Text("Hotjar site ID", help="Hotjar generated ID of your site")



