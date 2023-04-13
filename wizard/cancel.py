from odoo import api, fields, models, _


class CancelWiz(models.TransientModel):
    _name = "fleet.cancel.wiz"
    _description = "Cancel"

    name = fields.Char(string='Reason for Cancel', required=True)

    def action_fleet_cancel(self):
        for a in self:
            ctx = self._context
            rec = self.env[ctx.get('active_model')].browse(ctx.get('active_id'))
            rec.cancel_reason = a.name
            rec.state = 'cancelled'
            print("cancelled", ctx)

    # def action_print_excel_report(self):
    #     service = self.env['service.fleet'].search_read([])
    #     print(":::::::::::::::::::::::::",service)
    #
    #     data = {'service': service,
    #             'form_data': self.read()[0]
    #             }
    #     return self.env.ref('fleet_management.report_service_excel_card_xls').report_action(self, data=data)
