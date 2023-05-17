from odoo import fields, api, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, '%s %s %s' % (rec.title.name or " ", rec.name, rec.vat or "-",)))
            print("::::::::::", rec.title, rec.name, rec.vat)
            res = result
        print(result)
        return result

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100):
        # domain  '|' evaluation
        x = self.search(['|',('mobile', operator, name),'|',('category_id', operator, name,),('title', operator, name,)])
        return self.browse(x.ids).name_get()


