from odoo import fields, models
from datetime import datetime


class SlideSlidePartner(models.Model):
    _inherit = 'slide.slide.partner'

    invested_time = fields.Float("Time")
