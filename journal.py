# This file is part of sale_shop_invoice_journal module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pyson import Eval
from trytond.pool import PoolMeta

__all__ = ['Journal']
__metaclass__ = PoolMeta


class Journal:
    __name__ = 'account.journal'
    shops = fields.One2Many('sale.shop', 'journal', 'Shops',
            states={
                'invisible': Eval('type') != 'revenue',
            }, depends=['type'])
