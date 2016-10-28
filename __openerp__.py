# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2016- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Show address type for partners',
    'category': 'Utilities',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['base'],
    'description': """
Show address type for partners
==============================
* Adds a context parameter for toggling the showing of partner's address type below an m2o field
* Intended to make life easier in situations where the CRM contains partners that have similar/identical names for the main company and its delivery and invoice addresses
* Usage: <field name="partner_invoice_id" context="{ 'show_address_type': True }" options="{ 'always_reload': 1 }"/>
""",
    'data': [],
}
