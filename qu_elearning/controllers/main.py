from odoo import http
from odoo.http import request
from odoo.addons.website_slides.controllers.main import WebsiteSlides


class WebsiteSlidesQu(WebsiteSlides):

    def _prepare_additional_channel_values(self, values, **kwargs):
        values = super()._prepare_additional_channel_values(values, **kwargs)
        can_access = [e for e in request.env.user.groups_id if
                      values['channel'].allow_group_ids]
        values['can_access'] = bool(can_access)
        return values

    # @http.route(['/slides/channel/join'], type='json', auth='public', website=True)
    # def slide_channel_join(self, channel_id):
    #     success = super().slide_channel_join(channel_id)
    #     channel = request.env['slide.channel'].browse(channel_id)
    #     can_access = [e for e in request.env.user.groups_id if
    #                   channel.allow_group_ids]
    #     if channel.enroll != 'public' and not can_access:
    #         success.setdefault('error', 'Not Allowed')
    #     return success
