#!/usr/bin/env python
# This file is part of sale_shop_invoice_journal module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.tests.test_tryton import test_view, test_depends
import trytond.tests.test_tryton
import unittest


class SaleShopInvoiceJournalTestCase(unittest.TestCase):
    'Test Sale Shop Invoice Journal module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('sale_shop_invoice_journal')

    def test0005views(self):
        'Test views'
        test_view('sale_shop_invoice_journal')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleShopInvoiceJournalTestCase))
    return suite
