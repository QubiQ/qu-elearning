from odoo import http
from odoo.http import request
from odoo.addons.website_slides.controllers.main import WebsiteSlides


class WebsiteSlidesQu(WebsiteSlides):
    @http.route(
        ["/slides/update_invested_time"], type="json", auth="public", website=True
    )
    def update_invested_time(self, **post):
        user = request.env["res.users"].browse(request.uid)
        slide_id = int(post.get("slide_id"))
        slide_obj = (
            request.env["slide.slide.partner"]
            .sudo()
            .search(
                [("slide_id", "=", slide_id), ("partner_id", "=", user.partner_id.id)]
            )
        )
        # Convertting Miliseconds to hours
        time = int(post.get("time")) / 1000 / 60 / 60
        if slide_obj:
            slide_obj.write({"invested_time": slide_obj.invested_time + time})
        else:
            slide_obj.create(
                {
                    "partner_id": user.partner_id.id,
                    "slide_id": slide_id,
                    "invested_time": time,
                }
            )
