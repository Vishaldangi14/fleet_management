from odoo import api, fields, models, _


class CustomerWiz(models.TransientModel):
    _name = "customer.wiz"
    _description = "Customer Download"

    name = fields.Char(string='Customer Sheet Download')

    def action_report_customer_card_xls(self):
        self.ensure_one()
        [data] = self.read()
        data['emp'] = self.env.context.get('active_ids', [])
        customer = self.env['customer.fleet'].browse(self.env.context.get('active_ids', []))
        print("????????????????customer", customer)
        # print("///////////////search_count",search_count)
        datas = {
            'ids': [],
            'model': 'customer.fleet',
            'form': data
        }
        return self.env.ref('fleet_management.action_report_customer_card_xls').report_action(customer, data=datas)

    def action_report_customer_link(self):
        self.ensure_one()
        [data] = self.read()
        data['emp'] = self.env.context.get('active_ids', [])
        customer = self.env['customer.fleet'].browse(self.env.context.get('active_ids', []))
        print("????????????????customer", customer)
        # print("///////////////search_count",search_count)
        datas = {
            'ids': [],
            'model': 'customer.fleet',
            'view_mode': 'form',
            'form': data
        }
        return self.env.ref('fleet_management.action_report_customer_card_xls').report_action(customer, data=datas)
