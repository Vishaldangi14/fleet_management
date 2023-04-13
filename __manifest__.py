{
    'name': 'Fleet Management 4',
    'version': '15.0.1.0.1',
    'sequence': -100,
    'category': 'Fleet Management',
    'website': '',
    'summary': 'Fleet Management',
    'description': """Fleet Management""",
    'depends': ['base', 'mail', 'report_xlsx'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'report/report.xml',
        'data/mail_template.xml',
        'wizard/cancel_view.xml',
        'views/fleet_menu.xml',
        'views/staff_view.xml',
        'views/customer_view.xml',
        'views/services_view.xml',
        'views/vehicle_view.xml',

        # 'views/fleet_customer.xml',
    ],

    'demo': [
        'demo/fleet_demo.xml',
    ],

    'application': True,
    'license': 'LGPL-3',
}
