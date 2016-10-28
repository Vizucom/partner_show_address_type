# -*- coding: utf-8 -*-
from openerp import models, api, _


class ResPartner(models.Model):

    _inherit = 'res.partner'

    @api.multi
    def name_get(self):
        '''Append the address type to the end of the partner name, if
        the option is specified in the context'''
        res = super(ResPartner, self).name_get()

        if self.env.context.get('show_address_type', False):

            new_res = []
            for partner in res:
                id = partner[0]
                name = partner[1]
                partner_type = self.browse(id).type

                # Handle all separately to get translations for Odoo
                if partner_type == 'delivery':
                    name = '{} ({})'.format(name, _('delivery'))
                elif partner_type == 'invoice':
                    name = '{} ({})'.format(name, _('invoice'))
                elif partner_type == 'einvoice':
                    name = '{} ({})'.format(name, _('einvoice'))

                new_res.append((id, name))

            return new_res

        else:
            return res
