# Copyright 2021 Jesus Ramoneda <jesus.ramoneda@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class SlideChannelPartner(models.Model):
    _inherit = 'slide.channel.partner'

    blocked_access = fields.Boolean(string='Blocked')

    def toggle_block(self):
        for rec in self:
            rec.blocked_access = not rec.blocked_access

    def lock_access(self, access=True):
        for rec in self:
            rec.blocked_access = access


class SlideChannel(models.Model):
    _inherit = 'slide.channel'

    allow_group_ids = fields.Many2many(
        comodel_name='res.groups',
        relation='slide_channel_allowed_group_ids',
        string='Allowed Groups',
        help="Groups of users who can join without invitation")

    @api.depends('channel_partner_ids.partner_id')
    @api.model
    def _compute_is_member(self):
        channel_partners = self.env['slide.channel.partner'].sudo().search([
            ('channel_id', 'in', self.ids),
            ('blocked_access', '=', False),
        ])
        result = dict()
        for cp in channel_partners:
            result.setdefault(cp.channel_id.id, []).append(cp.partner_id.id)
        for channel in self:
            channel.is_member = channel.is_member = self.env.user.partner_id.id in result.get(
                channel.id, [])

    def _filter_add_members(self, target_partners, **member_values):
        allowed = super()._filter_add_members(target_partners, **member_values)
        on_invite = self.filtered(lambda channel: channel.enroll != 'public')
        new_allowed = self.env['slide.channel']
        users = target_partners.user_ids
        for group in users.groups_id:
            new_allowed += on_invite.filtered(
                lambda channel: group in channel.allow_group_ids)

        allowed |= new_allowed
        return allowed
