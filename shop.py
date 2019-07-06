# This file is part of sale_shop_invoice_journal module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['SaleShop']


class SaleShop(metaclass=PoolMeta):
    __name__ = 'sale.shop'
    journal = fields.Many2One('account.journal', 'Account Journal',
        domain=[('type', '=', 'revenue')])
