from odoo import models


class ReportXls(models.AbstractModel):
    _name = 'report.fleet_management.action_report_customer_card'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, customers):
        print("Customer excel report!!!!!!!!!!!!!!!!!!!!!!", customers, data)

        sheet = workbook.add_worksheet('customers')
        bold = workbook.add_format({'bold': True})
        row = 0
        col = 0

        sheet.write(row, col, 'Customer Name', bold)
        sheet.write(row, col + 1, 'Company Name', bold)
        sheet.write(row, col + 2, 'Age', bold)
        sheet.write(row, col + 3, 'Email', bold)
        sheet.write(row, col + 4, 'Gender', bold)
        sheet.write(row, col + 5, 'BirthDate', bold)
        sheet.write(row, col + 6, 'Contact', bold)
        sheet.write(row, col + 7, 'City', bold)
        sheet.write(row, col + 1, customers.name_id.name)
        # sheet.write(row,col + 1, 'Mobile no',bold)
        customers = self.env['customer.fleet'].search([])
        for s in customers:
            row = row + 1
            col = col
            sheet.write(row, col, s.name_id.name)
            sheet.write(row, col + 1, s.company.name_id)
            sheet.write(row, col + 2, s.age)
            sheet.write(row, col + 3, s.email)
            sheet.write(row, col + 4, s.gender)
            sheet.write(row, col + 5, s.birthdate)
            sheet.write(row, col + 6, s.contact)
            sheet.write(row, col + 7, s.city)