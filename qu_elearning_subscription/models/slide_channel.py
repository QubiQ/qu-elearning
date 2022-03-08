# Copyright 2021 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class SlideChannelPartner(models.Model):
    _inherit = "slide.channel.partner"

    blocked_access = fields.Boolean(string="Blocked")

    def toggle_block(self):
        for rec in self:
            rec.blocked_access = not rec.blocked_access

    def lock_access(self, access=True):
        for rec in self:
            rec.blocked_access = access


class SlideChannel(models.Model):
    _inherit = "slide.channel"

    @api.depends("channel_partner_ids.partner_id")
    @api.model
    def _compute_is_member(self):
        channel_partners = (
            self.env["slide.channel.partner"]
            .sudo()
            .search(
                [
                    ("channel_id", "in", self.ids),
                    ("blocked_access", "=", False),
                ]
            )
        )
        result = dict()
        for cp in channel_partners:
            result.setdefault(cp.channel_id.id, []).append(cp.partner_id.id)
        for channel in self:
            channel.is_member = (
                channel.is_member
            ) = self.env.user.partner_id.id in result.get(channel.id, [])
