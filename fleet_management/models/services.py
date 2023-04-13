from odoo import fields, api, models, _
from datetime import date


class Services(models.Model):
    _name = 'services.fleet'
    _description = 'Services details'
    _rec_name = 'vehicle_number'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name_id = fields.Many2one('vehicle.fleet', string="Car Name")
    car_name = fields.Char(string="Car Brand")
    car_model = fields.Char(string="Car Model")
    customer_ids = fields.Many2one("customer.fleet", string="Customer Name")
    vehicle_model = fields.Char(string="Vehicle_Model")
    vehicle_number = fields.Char(string="Vehicle Number")
    category = fields.Selection([('services', 'Services'), ('contract', 'Contract')], string="Car category")
    active = fields.Boolean(string="Active", default=True)
    book_date = fields.Date(string="Book Date")
    submit_date = fields.Date(string="Submit Date")
    chassis_number = fields.Text(string="Chassis Number")
    engine_number = fields.Text(string="Engine Number")
    pickup_location = fields.Char(string="Pickup Location")
    dropoff_location = fields.Char(string="Dropoff Location")
    customer_contact = fields.Char(string="Customer number")
    customer_complaint = fields.Char(string="Customer Complaint")
    rc_book_number = fields.Text(string="RC Book Number")
    image = fields.Binary(string='Image')
    payment = fields.Float(string='Amount', default='1')

    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    states = fields.Char(string='State')
    zip = fields.Char(string='Zip')
    country = fields.Char(string='Country')
    state = fields.Selection([('draft', 'Start'),
                              ('process', 'Process'),
                              ('done', 'Done',),
                              ('cancelled', 'Cancelled')],
                             default='draft', string="Status", required='true', )

    cancel_reason = fields.Char(string='Reason for Cancellation')

    # def _compute_payment(self):
    #     for rec in self:
    #         if rec.category == "contract":
    #             rec.payment = "70000"
    #         elif rec.category == "services":
    #             rec.payment = "30000"
    #         else:
    #             rec.payment = 0

    def action_view_payment(self):
        print()

        #:::::::::::::: many2 one use hoga
        #

    def test_done(self):
        print("<<<<<<<<<<<<<<<<<<Button Search>>>>>>>>>>>>>>>>>>>")
        for a in self:
            services_obj = self.env['services.fleet']
            print(":::::::::::: services_obj::::::::::::::", services_obj)
            services_obj.create({
                'name_id': self.name_id,
                'category': self.category,
                'payment': self.payment,
                'active': self.active,
                'rc_book_number': self.rc_book_number,
                'state': 'done'
            })
            a.state = "done"

    # ::::::::::::::::::::form view open Code ::::::::::::::

    category_count = fields.Integer(string='category', compute='_compute_test_service')

    @api.depends('category_count')
    def _compute_test_service(self):
        for res in self:
            category_count = self.env['services.fleet'].search_count([('category', '=', 'contract')])
            print("---------services----------", category_count)
            res.category_count = category_count
            print("::::::::::::::::res.category_count::::::::::", res.category_count)
            print("|||||||||||res.services||||||||||||", category_count)

    def action_view_services(self):
        self.ensure_one()
        print("self:::::", self)
        print("self:::id::", self.id)
        print("self::ids:::", self.ids)
        records = {
            'type': 'ir.actions.act_window',
            'name': 'Car category',
            'res_model': 'services.fleet',
            'view_mode': 'tree,form',
            'domain': [('category', '=', 'contract')],
            'context': dict(self._context, create=False)
        }
        if self.category_count == 1:
            action = self.env['services.fleet'].search([('category', '=', 'contract')])
            records.update({
                'view_mode': 'form',
                'res_id': action.id,
            })
        print("records::::::::", records)
        return records

    # def action_in_progress(self):
    #     self.write({'customer_ids': [(0, 0, {'category': "contract",})]})
    #     print("Button Click !!!!!!!!!!!!!")

    def action_delete(self):
        # for a in self:
        #     ctx=self._context
        self.write({'customer_ids': [(5, 2, False)]})
        print("Button Click !!!!!!!!!!!!!>>>>>>>::::>button delete:::::>>>>>>>>>>>>>>>>", )

    # @api.model
    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         name_id = rec.name_id
    #         display_name = "Custom Display Name for {}".format(name_id)
    #         result.append((rec.id, display_name))
    #     return result

    def name_get(self):
        result = []
        print("self", self)
        for rec in self:
            result.append((rec.id, '%s - %s %s %s' % (
                rec.name_id.model_name, rec.vehicle_number or " ", rec.chassis_number or "-",
                rec.engine_number or " ",)))
            print(":::::::::::::res====::::::::::::", rec.id, rec.vehicle_number, rec.chassis_number,
                  rec.engine_number)
            print(result)
        return result

    @api.onchange('category')
    def onchange_category(self):
        for rec in self:
            if rec.category == "contract":
                rec.payment = 70000
            elif rec.category == "services":
                rec.payment = 30000
            else:
                rec.payment = 0

    per_month = fields.Float(string="per month payment", compute="_compute_payamet_par_month", default=0.0)

    installment = fields.Selection(
        [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
         ('6', '6')], default="1", string='Installment')

    @api.depends("installment", "per_month")
    def _compute_payamet_par_month(self):
        for record in self:
            if record.installment != 0:
                record.per_month = record.payment / int(record.installment)
            else:
                record.per_month = 0
                print(record.per_month)
