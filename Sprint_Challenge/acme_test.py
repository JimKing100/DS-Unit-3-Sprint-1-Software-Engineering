# !/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_stealability(self):
        """Test default stealability."""
        prod = Product('Test Product', price=10, weight=40)
        self.assertEqual((prod.price / prod.weight), 0.25)

    def test_default_explode(self):
        """Test default explode."""
        prod = Product('Test Product', weight=40, flammability=2.0)
        self.assertEqual((prod.flammability * prod.weight), 80)


if __name__ == '__main__':
    unittest.main()
