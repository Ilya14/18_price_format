import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_price(self):
        test_prices = ['3245.000000', '-3245.000000', '3245.1399', '-3245.1399', '123456.999']
        formatted_prices = ['3 245', '-3 245', '3 245,14', '-3 245,14', '123 457']
        for test_pair in zip(test_prices, formatted_prices):
            with self.subTest(test_pair=test_pair):
                self.assertEqual(format_price(test_pair[0]), test_pair[1])

    def test_incorrect_price_raises(self):
        incorrect_prices = ['3 245.000000', '3245,000000', 'abc', '- 3245.1399']
        for incorrect_price in incorrect_prices:
            with self.subTest(incorrect_price=incorrect_price), self.assertRaises(ValueError):
                format_price(incorrect_price)


if __name__ == '__main__':
    unittest.main()
