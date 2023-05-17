from odoo import fields, api, models, _
from datetime import date


class Customer(models.Model):
    _name = 'customer.fleet'
    _rec_name = 'partner_id'
    _description = 'customer details'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    partner_id = fields.Many2one('res.partner', string='Customer Name')
    company = fields.Many2one('vehicle.fleet', string="Company Name")
    car_name = fields.Char(string="Car Brand")
    age = fields.Integer(string='Age', compute="_compute_age")
    email = fields.Char(string='Email')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    birthdate = fields.Date(string='Birthdate', copy=False)
    mobile = fields.Integer(string='Mobile')
    image = fields.Image(string='Image')
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    zip = fields.Char(string='Zip')
    country = fields.Many2one('res.country', string='Country')
    states = fields.Many2one('res.country.state', string='State')
    length_visibility = fields.Boolean("visibility", compute="compute_field_visibility", default=False, store=True)
    customer_seq = fields.Char(required=True, readonly=True, default=lambda self: _('New'))

    def test_recordset(self):
        for rec in self:
            partners = self.env['customer.fleet'].search([])
            print(":::::::::<<<<<>>search>>>>>>>>>::::::::::::", partners)
            print(":::::::::::::::::<<<<<<<<<<<<<map>>>>>>>>>>>>>", partners.mapped("email"))
            print("::::::::::::::::<<<<<<<<<<partners filtered>>>>>>>>>", partners.filtered(lambda rec: rec.partner_id))

    # @api.depends('division_name')
    # def _compute_division_name(self):
    #     for rec in self:
    #         division_name = self.env['customer.fleet'].read_group(domain=[('total_gender', "=", 'A')],
    #                                                             fields=['gender_id'], groupby=['gender_id'])
    #
    #         print('>>>>>>>>>>>division_name', division_name)
    #         rec.division_name = 1

    def _compute_age(self):
        for rec in self:
            today = date.today()
            # print("::::::::::::::::today:::::::::",today)
            if rec.birthdate:
                rec.age = today.year - rec.birthdate.year
            else:
                rec.age = 0

    # def action_view_customer(self):
    #     for rec in self:
    #         return {
    #             'type': 'ir.actions.act_window',
    #             'view_mode': 'tree',
    #             'res_model': 'customer.fleet',
    #             # 'views': [(False, 'tree')],
    #             'views': [(False, 'tree'),(False, 'form')],
    #             'view_id': False,
    #             'domain': [('gender', '=','male')],
    #         }

    # def action_view_customer(self):
    #     self.ensure_one()
    #     print("::::::::::::::<<<<<<<<<<<<<insure_one>>>>>>:::::::::::::::::::")
    #     print("<<<<<<<<<<<<self.gender:::::::::::::::", self.gender)
    #     records = {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Gender',
    #         'res_model': 'customer.fleet',
    #         'view_mode': 'tree,form',
    #         'domain': [('gender', '=', 'female')],
    #         'context': dict(self._context, create=False)
    #     }
    #     if self.gender == 1:
    #         record = self.env['customer.fleet  '].search([('gender', '=', 'female')])
    #         records.update({
    #             'view_mode': 'form',
    #             'res_id': record.id,
    #         })
    #     print("<<<<<<<<<<<<<customer.record::::::::", records)
    #     return records

    def _compute_customer(self):
        for res in self:
            customers = self.env['customer.fleet'].search_count([('customers', '=', res.id)])
            print("---------customer----------", customers)

            res.customers = customers
            print("|||||||||||res.customer||||||||||||", customers)

    def action_view_customer(self):
        for rec in self:
            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'tree',
                'res_model': 'customer.fleet',
                'views': [(False, 'tree')],
                'view_id': False,
                # 'domain': [('gender', '=', 'male')],
            }

    @api.model
    def default_get(self, fields):
        print("::::::::::::::<<<<<default method>>>>:::::::::", fields)
        res = super(Customer, self).default_get(fields)
        print("::::::::::<<<<<<default method> ??????????/>>>>>>>", res)
        customer_rec = self.env['customer.fleet'].search([('gender', '=', 'male')], limit=5, order='id desc')
        print(":::::::::::::::::>>>>>>>>>>>>>::::::::::::", customer_rec)
        # res['country'] = 'india'
        return res

    # @api.model
    # def compute_field_visibility(self):
    #     """ compute function for the visibility of the fields """
    #     for rec in self:
    #         if self.env.user.has_group('fleet_management.group_fleetmanagement_customer'):
    #             test = rec.length_visibility = False
    #             print('test------------------------>>>>>>>>>>>>>>>>>>>>>>>>>>>', test)

    # -----------ir.squence------------

    #
    # @api.model
    # def create(self, vals):
    #     # print("Customer Code::::::::::::::",vals)
    #
    #     vals['customer_seq'] = self.env['ir.sequence'].next_by_code('customer.fleet')
    #     # print("vals['customer_seq']::::::::::::::::::::::::::",vals['customer_seq'])
    #     result = super(Customer, self).create(vals)
    #     # print("Result:::::::::::::::::",result)
    #
    #     return result

    # -----------ir.squence-----------

    def sale_order(self):
        self.ensure_one()
        rec = {
            'type': 'ir.actions.act_window',
            'name': 'Customer Fleet',
            'res_model': 'sale.order',
            'view_mode': 'tree,form',
            'domain': [('partner_id', '=', self.partner_id.id)],
            'context': dict(self._context, create=False)
        }
        return rec

    @api.onchange('partner_id')
    def _onchange_email_mobile(self):
        if self.partner_id:
            self.email = self.partner_id.email
            self.mobile = self.partner_id.mobile

    customer_service = fields.Integer(compute='compute_count_services')

    def compute_count_services(self):
        for rec in self:
            rec.customer_service = self.env['services.fleet'].search_count(
                [('customer_id', 'in', rec.ids)])

    def action_view_services(self):
        self.ensure_one()
        print("self.id", self.id)
        rec = {
            'type': 'ir.actions.act_window',
            'name': 'service fleet',
            'res_model': 'services.fleet',
            'view_mode': 'tree,form',
            'domain': [('customer_id', '=', self.id)],
            'context': dict(self._context, create=False)

        }
        return rec

    @api.model
    def create(self, vals):
        vals['customer_seq'] = self.env['ir.sequence'].next_by_code('customer.fleet') or _('New')
        res = super(Customer, self).create(vals)
        return res

