# This file is part of sale_shop_invoice_journal module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Sale']


class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'

    def _get_invoice_sale(self):
        invoice = super(Sale, self)._get_invoice_sale()
        journal = self.shop and self.shop.journal
        if journal:
            invoice.journal = journal
        return invoice
