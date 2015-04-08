# This file is part of sale_shop_invoice_journal module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'
    journal = fields.Many2One('account.journal', 'Account Journal',
        domain=[('type', '=', 'revenue')])

    def _get_invoice_sale(self, invoice_type):
        invoice = super(Sale, self)._get_invoice_sale(invoice_type)
        journal = self.journal
        if journal:
            invoice.journal = journal
        return invoice

    @staticmethod
    def default_journal():
        pool = Pool()
        Journal = pool.get('account.journal')
        User = pool.get('res.user')
        user = Transaction().user
        user = User(user)
        shop = user.shop
        if shop and shop.journal:
            return shop.journal.id

        journals = Journal.search([
                ('type', '=', 'revenue'),
                ('sequences', '=', None),
                ], limit=1)
        if journals:
            journal, = journals
            return journal.id
        journals = Journal.search([
                ('type', '=', 'revenue'),
                ], limit=1)
        if journals:
            journal, = journals
            return journal.id

    def on_change_shop(self):
        res = super(Sale, self).on_change_shop()
        shop = self.shop
        if shop and shop.journal:
            res['journal'] = shop.journal.id
        else:
            journal = self.default_journal()
            if journal:
                res['journal'] = journal
        return res
