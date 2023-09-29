
{
    'name': 'QubiQ E-Learning',
    'summary': 'QubiQ E-Learning Base',
    'version': '16.0.1.0.0',
    'category': 'Knowledge',
    'author': 'QubiQ',
    'website': 'https://www.qubiq.es',
    'depends': [
        "website_slides"
    ],
    "data": [
        'views/slide_channel_partner_view.xml',
        'views/slide_channel_view.xml',
        'views/slide_slide_partner.xml',
        #'views/website_slides_templates_course.xml',
        'security/ir_rule.xml',
        ],
    'application': True,
    'installable': True,
}
