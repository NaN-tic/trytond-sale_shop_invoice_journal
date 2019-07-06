# This file is part of sale_shop_invoice_journal module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import shop
from . import journal
from . import sale


def register():
    Pool.register(
        journal.Journal,
        shop.SaleShop,
        sale.Sale,
        module='sale_shop_invoice_journal', type_='model')
