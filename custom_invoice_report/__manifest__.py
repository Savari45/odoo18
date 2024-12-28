{
    'name': 'Custom Invoice Report',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Custom invoice report with outstanding credits and PD cheques',
    'description': 'This module customizes the invoice report to include outstanding credits and post-dated cheques.',
    'author': 'Your Name',
    'depends': ['account', 'base', 'sale'],
    'data': [
        'report/custom_invoice_report.xml',
        'report/custom_ipos_nvoice_report.xml'

    ],
    'installable': True,
    'application': False,
}
