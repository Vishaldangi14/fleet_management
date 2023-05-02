{
    'name': 'Fleet Management1',
    'version': '15.0.1.0.1',
    'sequence': -100,
    'category': 'Fleet Management1',
    'website': '',
    'summary': 'Fleet Management',
    'description': """Fleet 1""",
    'depends': ['base', 'mail', 'report_xlsx'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'report/report.xml',
        'report/services_report.xml',
        'wizard/cancel_view.xml',
        'data/data.xml',
        'data/mail_template.xml',
        'data/mail_template_services.xml',
        'views/fleet_menu.xml',
        'views/staff_view.xml',
        'views/customer_view.xml',
        'views/services_view.xml',
        'views/vehicle_view.xml',


    ],

    'demo': [
        'demo/fleet_demo.xml',
    ],

    'application': True,
    'license': 'LGPL-3',
}
