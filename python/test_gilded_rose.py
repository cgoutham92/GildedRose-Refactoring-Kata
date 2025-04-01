# -*- coding: utf-8 -*-
import unittest
from gilded_rose import DefaultItem


class TestGildedRose(unittest.TestCase):

    def test_default_item(self):
        # Create a normal item with initial values
        item = DefaultItem("foo", 1, 10)

        # First update (sell_in = 1)
        item.update()  # sell_in will become 0, and quality should decrease by 1
        self.assertEqual(item.quality, 9)
        self.assertEqual(item.sell_in, 0)

        # Second update (sell_in = 0)
        item.update()  # sell_in will become -1, and quality should decrease by 2
        self.assertEqual(item.quality, 7)
        self.assertEqual(item.sell_in, -1)

        # Test that quality does not go below 0
        item.quality = 0
        item.update()
        self.assertEqual(item.quality, 0)


if __name__ == '__main__':
    unittest.main()
