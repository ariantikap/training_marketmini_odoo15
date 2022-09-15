# -*- coding: utf-8 -*-
{
    'name': "arishop",

    'summary': """
        odoo module for marketmini store""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menuroot.xml',
        'views/produk_view.xml',
        'views/jenisproduk_view.xml',
        'views/pegawai_view.xml',
        'views/kasir_view.xml',
        'views/pelayan_view.xml',
        'views/supervisor_view.xml',
        'views/transaksi_view.xml',
        'views/konsumen_view.xml',
        'views/supplier_view.xml',
        'report/report.xml',
        'report/print_faktur_transaksi.xml',
        'report/wizard_transaksireport_tmp.xml',
        'wizard/produkdatangwizard_view.xml',
        'wizard/transaksireportwizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
