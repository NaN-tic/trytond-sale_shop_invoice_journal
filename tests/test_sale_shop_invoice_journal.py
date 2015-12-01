# This file is part of the sale_shop_invoice_journal module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleShopInvoiceJournalTestCase(ModuleTestCase):
    'Test Sale Shop Invoice Journal module'
    module = 'sale_shop_invoice_journal'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleShopInvoiceJournalTestCase))
    return suite