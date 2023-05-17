from odoo import fields, api, models, _
from datetime import date
from odoo.exceptions import UserError, ValidationError


class Staff(models.Model):
    _name = 'staff.fleet'
    _description = 'staff details'
    _name_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Many2one('customer.fleet', string='Employee Name')
    age = fields.Integer(string='Age', compute="_compute_age")
    email = fields.Char(string='Email')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    birthdate = fields.Date(string='Birthdate', copy=False)
    contact = fields.Integer(string='Contact')
    image = fields.Binary(string='Image')
    active = fields.Boolean(string="Active", default=True)
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street2')
    city = fields.Char(string='City')
    states = fields.Char(string='State')
    zip = fields.Char(string='Zip')
    country = fields.Char(string='Country')

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birthdate:
                rec.age = today.year - rec.birthdate.year
            else:
                rec.age = 0

    # @api.model(birthdate)
    # def _contains(self):
    #     for rec in self:
    #         today = date.today()
    #     if rec.birthdate < today:
    #         raise ValidationError("sdfghjkjhgfghj")

    # @api.onchange('name')
    # def _onchange_contact(self):
    #     self.email = False
    #     self.contact = False
    #     self.gender = False
    #     self.birthdate = False
    #     self.age = False
    #     self.country = False
    #     self.street2 = False
    #     self.street = False
    #     self.image = False

    @api.model
    def create(self, vals):
        res = super(Staff, self).create(vals)
        print(":::::::::::::::res:::::::::::", res)
        res.update({'contact': '810740490'})
        return res

    #
    def write(self, vals):
        print(self)
        print("<<<<<<<<<write>>>>>>", vals)
        res = super(Staff, self).write(vals)
        print(":::::::::::::res::::::::::::", res)
        return res

    def unlink(self):
        print("<<<<unlink method>>>>>>>>>>")
        res = super(Staff, self).unlink()
        print("<:::::::::::::::res::::::::::::::::>", res)
        return res

    # def copy(self, default=None):
    #     print(">>>>>>>>>>>>>>>>>>>copy method")
    #     res = super(Staff, self).copy(default)
    #     res.name="name [copy]"
    #     return res

    note = fields.Char(string="Remarks")

    def copy(self, default=None):
        print("Success")
        if default is None:
            default = {}
            print(">>>>>>>>>>>>>>>>>", default)
        if not default.get('name'):
            default['name'] = "copy"
            default['note'] = "All ready exist"
            res = super(Staff, self).copy(default)
            print(">>.>>>>>>>>>>befor>>>>>", res.name)
        return res

    # def _compute_kpi_staff_fleet(self):
    #     if not self.env.user.has_group('account.group_account_invoice'):
    #         raise AccessError(_("Do not have access, skip this data for user's digest email"))
    #

    # @api.model
    # def create(self, vals):
    #     # if not vals.get('note'):
    #     #     vals['note'] = 'new student'
    #     if vals.get('customer_seq', ('New')) == ('New'):
    #         vals['customer_seq'] = self.env['ir.sequence'].next_by_code('staff.fleet') or _('New')
    #         res = super(Staff, self).create(vals)
    #         return res
