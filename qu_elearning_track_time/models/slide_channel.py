# Copyright 2021 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models

# Cheat maybe used in FUNDAE protocol
# def set_track_time(self):
#     for rec in self:
#         time = random.uniform(
#             0.75*rec.slide_id.completion_time, 1.25*rec.slide_id.completion_time)
#         rec.write({'track_time': time})


class SlideChannelPartner(models.Model):
    _inherit = "slide.channel.partner"

    time_invested = fields.Float(string='Minutes',
                                 compute="_compute_time_invested")

    def _compute_time_invested(self):
        for rec in self:
            rec.time_invested = sum(self.env['slide.slide.partner'].\
                                    search([('channel_id', '=', rec.id),
                                            ('partner_id', '=', rec.partner_id.id)]).\
                                                mapped('invested_time'))

    def get_slide_time(self):
        return {
            'name': 'Slide Time',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'slide.slide.partner',
            'target': 'current',
            'view_id': self.env.ref(
                'qu_elearning_track_time.slide_slide_partner_tree_view')[0].id,
            'domain': [('partner_id', '=', self.partner_id.id),
                        ('channel_id','=',self.channel_id.id)]
        }


class SlideChannel(models.Model):
    _inherit = "slide.channel"

    total_time_invested_count = fields.Float(compute="compute_total_time")

    def compute_total_time(self):
        for rec in self:
            rec.total_time_invested_count = sum(self.env['slide.slide.partner'].\
                                    search([('channel_id', '=', rec.id)]).mapped('invested_time'))

    def total_time_invested(self):
        return {
            'name': 'Slide Time',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree',
            'res_model': 'slide.slide.partner',
            'view_id': self.env.ref(
                'qu_elearning_track_time.slide_slide_partner_tree_view')[0].id,
            'target': 'current',
            'domain': [('channel_id', '=', self.id), ('invested_time', '!=', 0)]
             }
