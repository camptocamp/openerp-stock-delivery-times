# -*- encoding: utf-8 -*-
#################################################################################
#                                                                               #
#    stock_delivery_delays_working_days for OpenERP                                          #
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

from osv import osv, fields
import netsvc
import time
from datetime import date
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
from tools.translate import _
from tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

class delivery_carrier(osv.osv):

    _inherit = "delivery.carrier"

    _columns = {
        'delivery_lead_time': fields.integer('Delivery Lead Time'),
        'calendar_id': fields.many2one("resource.calendar", "Carrier Working time"),
    }

    _defautls = {
    }

delivery_carrier()