from odoo import api, models, fields, _


class ReportCustomerReport(models.AbstractModel):
    _name = 'report.fleet_management.report_customer_id_card'
    _description = 'Account Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        print("testing------------------------------------------")
        docs = self.env['customer.fleet'].search([])
        return {
            'docs': docs,
        }
