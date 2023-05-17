from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_id = fields.Many2one('sale.order', string="")
    related_sale_service_id = fields.Many2one('services.fleet', string='services', readonly=True,
                                              related='sale_id.service_id', store=True)

