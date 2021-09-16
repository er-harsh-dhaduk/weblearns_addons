# -*- coding: utf-8 -*-
{
    'name': 'Odoo Datafile Tutorial',
    'version': '14.0.0.1.0',
    'summary': 'CSV vs XML data file Tutorial',
    'sequence': -111,
    'description': 'CSV vs XML data file Tutorial',
    'category': 'Tutorials',
    'author': 'Weblearns',
    'maintainer': 'Weblearns',
    'website': 'https://googlyengineer.blogspot.com',
    'live_test_url': 'https://www.youtube.com/playlist?list=PLAR8TpPnVeTQi9q1vca1c52rnITF7wtwM',
    'license': 'LGPL-3',
    'depends': [
        'website_slides'
    ],
    'data': [
        'data/channel_data.xml',
        'data/slide_data.xml'
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True
}
