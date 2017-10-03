#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from crypto_price_rss.cli import main


class TestCryptoPriceRSS(unittest.TestCase):
    def test_generate_response(self):
        # stupid simple test to not throw exception
        main()
