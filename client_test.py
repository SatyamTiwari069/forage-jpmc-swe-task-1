import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Test for stock ABC
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 120.48)
        self.assertEqual(ask_price, 121.2)
        self.assertEqual(price, (120.48 + 121.2) / 2)

        # Test for stock DEF
        stock, bid_price, ask_price, price = getDataPoint(quotes[1])
        self.assertEqual(stock, 'DEF')
        self.assertEqual(bid_price, 117.87)
        self.assertEqual(ask_price, 121.68)
        self.assertEqual(price, (117.87 + 121.68) / 2)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Test for stock ABC where bid price is greater than ask price
        stock, bid_price, ask_price, price = getDataPoint(quotes[0])
        self.assertEqual(stock, 'ABC')
        self.assertEqual(bid_price, 120.48)
        self.assertEqual(ask_price, 119.2)
        self.assertEqual(price, (120.48 + 119.2) / 2)

    def test_getRatio(self):
        # Normal case
        self.assertEqual(getRatio(120, 60), 2)

        # Division by zero
        self.assertIsNone(getRatio(120, 0))

        # Division with floats
        self.assertAlmostEqual(getRatio(120.0, 60.0), 2.0)

        # Negative values
        self.assertAlmostEqual(getRatio(-120.0, 60.0), -2.0)



if __name__ == '__main__':
    unittest.main()
