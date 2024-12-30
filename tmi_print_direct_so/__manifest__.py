# -*- coding: utf-8 -*-
###################################################################################
#
#    Copyright (c) 2023 tmistones.com
#
#
#
###################################################################################

{
    "name": "TMI direct print SO",
    "summary": """Help you print SO, Quotation instantly to system printer without converting to PDF!""",
    "version": "18.0.1.0.0",
    "category": "Report",
    "website": "https://tmistones.com",
    'price': "0",
    'currency': "USD",
    'live_test_url': 'https://report.tmistones.com',
    "author": "TMI Teamwork",
    "contributors": [
        u"Vũ Ngọc Tuyến <https://tuyenvn4649.github.io/>",

    ],
    "depends": [
        'sale'
    ],
    "data": [
        'security/res_groups.xml',
        "views/view.xml",
    ],
    'assets':{
    },
    'demo': [

    ],
    "images": [
        "static/description/tmi_print_direct_so_banner.png",
        "static/description/tmi_print_direct_so_screenshot.png"
    ],
    "external_dependencies": {},
    "application": True,
    "installable": True,
    "license": 'LGPL-3',
    'assets': {
            'web.assets_backend': [

                'tmi_print_direct_so/static/src/js/print_direct.js',
            ],
            'web.report_assets_common': [
            ],

        },

}
