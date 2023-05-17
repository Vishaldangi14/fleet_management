from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    service_id = fields.Many2one('services.fleet', string="Service")

