
{
    'name': 'YourHome Theme',
    'description': 'YourHome website theme',
    'category': 'Theme',
    'sequence': 10,
    'version': '1.0',
    'depends': ['website'],
    'data': [
        'views/header.xml',
        'views/homepage.xml',
        # 'views/custom_footer.xml',
    ],
    'assets':{
        'web.assets_frontend': [
            'hm_school_website/static/src/scss/styles.scss',
            'hm_school_website/static/src/css/styles.css',
        ],
        'web._assets_primary_variables': [
            "hm_school_website/static/src/scss/primary_variables.scss",
        ]
    },
    'images': [
    ],
    'snippet_lists': {
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
