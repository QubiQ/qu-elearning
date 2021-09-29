from odoo import api, fields, models


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    def write(self, values):
        # Add code here
        res = super().write(values)
        self.env['slide.channel.partner'].search([
            ('channel_id.enroll', '=', 'payment'),
            ('channel_id.product_id', 'in',
                self.recurring_invoice_line_ids.mapped('product_id.id')),
            ('partner_id', '=', self.partner_id.id)
        ]).lock_access(self.to_renew)
        return res
