{
    "name": "QubiQ E-Learning Track Time",
    "summary": "Track the time of the E-learning Students",
    "version": "16.0.1.0.0",
    "category": "Knowledge",
    "author": "QubiQ",
    "website": "https://www.qubiq.es",
    "depends": ["website_slides", "qu_elearning"],
    "assets": {
        "web.assets_frontend": [
            "qu_elearning_track_time/static/src/js/time_elearning.js"
        ]
    },
    "data": [
        "views/slide_channel.xml",
        "views/website_slides_templates_course.xml",
        "views/slide_slide_partner.xml",
    ],
    "application": True,
    "installable": True,
}
