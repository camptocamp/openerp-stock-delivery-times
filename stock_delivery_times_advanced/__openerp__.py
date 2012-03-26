# -*- encoding: utf-8 -*-
#################################################################################
#                                                                               #
#    stock_delivery_delays_advanced for OpenERP                                          #
#    Copyright (C) 2011 Akretion Benoît Guillot <benoit.guillot@akretion.com>   #
#                                                                               #
#    This program is free software: you can redistribute it and/or modify       #
#    it under the terms of the GNU Affero General Public License as             #
#    published by the Free Software Foundation, either version 3 of the         #
#    License, or (at your option) any later version.                            #
#                                                                               #
#    This program is distributed in the hope that it will be useful,            #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the              #
#    GNU Affero General Public License for more details.                        #
#                                                                               #
#    You should have received a copy of the GNU Affero General Public License   #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.      #
#                                                                               #
#################################################################################


{
    'name': 'stock_delivery_delays_advanced',
    'version': '0.1',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': """empty""",
    'author': 'Akretion',
    'website': 'http://www.akretion.com/',
    'depends': ['sale','purchase_to_sale','stock_delivery_times_working_days'], 
    'init_xml': [],
    'update_xml': [ 
           'stock_view.xml',
           'sale_view.xml',
           'product_view.xml',
           'product_data.xml',
           'wizard/stock_change_date_view.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}

