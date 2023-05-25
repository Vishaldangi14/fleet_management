from odoo import api, models, fields, _


class ReportCustomerReport(models.AbstractModel):
    _name = 'report.fleet_management.sale_parser_id'
    _description = 'Account Report'

    def _get_data(self, o):
        # data_dict = {}
        data_list = []
        ServicesFleet = self.env["services.fleet"]
        SaleOrder = self.env["sale.order"]
        DeliveryOrder = self.env["stock.picking"]
        Accountmove = self.env["account.move"]

        service_ids = ServicesFleet.search([('customer_id', '=', o.id)])
        print("service_ids", service_ids)
        # so_ids = SaleOrder.search([("service_id", "in", service_ids.ids)])
        # print("so_ids", so_ids)
        for service in service_ids:
            so_id = SaleOrder.search([("service_id", "=", service.id)])
            delivery_id = DeliveryOrder.search([("related_sale_service_id", "=", service.id)])
            paid_amount = 0
            amount_total = 0
            amount_due = 0

            invoice_ids = so_id.invoice_ids
            print("invoice_ids:::::::::::::::::", invoice_ids)
            invoice_list = []
            order_list = []
            for order in so_id:
                print("order??????:15:::::::::::?????", order)
                print(":::::::::::order:::::", order.name)
                o = order_list.append(order.name)
                print("OOIOVndhvbshjvbagcvag", o)
                print("orderlist::::::::", order_list)
                print(" ".join(order_list))

            for invoice in invoice_ids:
                print("invoice_ids///12////", invoice)
                print("name???", invoice.name)
                v = invoice_list.append(invoice.name)
                print("v///////////////", v)

                print("paid_amount", paid_amount)
                amount_total += invoice.amount_total
                amount_due += invoice.amount_residual
                print("invoice_due", amount_due)
                print("amount_total", amount_total)
            paid_amount = amount_total - amount_due
            print("paid_amount", paid_amount)

            # 5 / 0
            print("invoice_list", invoice_list)
            print(" ,".join(invoice_list))

            data_list.append({
                "service_name": service.services_seq,
                # "so_name": " ".join(order_list),
                "so_name": ",".join(so_id.mapped("name")),
                "delivery": delivery_id.name,
                # 'invoice': ", ".join(invoice_list),
                'invoice': ", ".join(invoice_ids.mapped("name")),
                'amount_total': amount_total,
                'amount_paid': paid_amount,
                'amount_due': amount_due,
            })

        return data_list

    @api.model
    def _get_report_values(self, docids, data=None):
        print("<<<<<<<<<docids|||||||||||????", docids)
        print(":::::::::::::::::::::::::::::::::::::::::::||||data|||||||????", data)
        SaleOrder = self.env["sale.order"].browse(docids)
        DeliveryOrder = self.env["stock.picking"].browse(docids)
        ServicesFleet = self.env["services.fleet"].browse(docids)
        AccountMove = self.env["account.move"].browse(docids)
        docs = self.env['customer.fleet'].browse(docids)

        return {
            'docs': docs,
            'get_data': self._get_data,

        }
