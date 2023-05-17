from odoo import fields, api, models, _
from datetime import date


class Vehicle(models.Model):
    _name = 'vehicle.fleet'
    _description = 'Vehicles'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string=" Car Model Name")
    vehicle_type = fields.Selection([('car', 'Car'), ('bike', 'Bike')], string="Category")
    model_year = fields.Integer()
    color = fields.Char()
    # vehicle_name = fields.Char(string="Vehicle Name",related ='name')
    image = fields.Binary(string="Image")
    seats = fields.Integer(string='Seats')
    doors = fields.Integer(string='Doors')
    trailer_hitch = fields.Boolean(string="Trailer Hitch", default=True)
    full_type = fields.Selection([('diesel', 'Diesel'), ('petrol', 'Petrol'), ('cng', 'Cng'), ('electric', 'Electric')],
                                 string="Fuel Type")
    power = fields.Integer(string="Power")
    horsepower = fields.Integer(string="Horsepower")
    horsepower_tax = fields.Float(string="Horsepower Tax")
    vendors = fields.Many2one('services.fleet', string="Vendors")
    transmission = fields.Selection([('manual', 'Manual'), ('automatic', 'Automatic')], string="Transmission")

    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super().fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,
                                      submenu=submenu)
        print(":::::::::::::::::res::::::::::::::", res)
        print(":::::::::::::>>>>>>>>self:::::::::::::<<<<<<<", self)

        return res

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        x = self.search(['|', ('color', operator, name), '|', ('horsepower', operator, name,), '|',
                         ('transmission', operator, name), '|', ('horsepower_tax', operator, name),
                         ('doors', operator, name)])
        return self.browse(x.ids).name_get()
