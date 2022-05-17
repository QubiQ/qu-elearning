# Copyright 2021 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
import random

class SlideSlidePartner(models.Model):
    _inherit = 'slide.slide.partner'

    track_time = fields.Float("Track Time")

    # Cheat
    def set_track_time(self):
        for rec in self:
            time = random.uniform(
                0.75*rec.slide_id.completion_time, 1.25*rec.slide_id.completion_time)
            rec.write({'track_time': time})
    