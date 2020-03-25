# -*- coding: utf-8 -*-
{
    'name': "fruteria",

    'summary': """
        Módulo personal para gestión de una frutería""",

    'description': """
        Módulo personal para la gestión de una frutería que gestionará frutas, socios y peticiones, estas últimas restringidas a un tipo de fruta por petición.
    """,

    'author': "Román Arufe Blanco",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/socio.xml',
        'views/peticion.xml',
        'views/fruta.xml',
        'views/lineapeticion.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}