# -*- coding: utf-8 -*-
import unittest
from gilded_rose import DefaultItem, AgedBrie, BackstagePass


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

    def test_aged_brie(self):
        # Create an Aged Brie item
        item = AgedBrie("Aged Brie", 1, 10)

        # First update (sell_in = 1)
        item.update()  # sell_in becomes 0, quality increases by 1
        self.assertEqual(item.quality, 11)
        self.assertEqual(item.sell_in, 0)

        # Second update (sell_in = 0)
        item.update()  # sell_in becomes -1, quality increases by 2
        self.assertEqual(item.quality, 13)
        self.assertEqual(item.sell_in, -1)

        # Test that quality never exceeds 50
        item.quality = 70
        item.update()
        self.assertEqual(item.quality, 50)  # Quality should remain 50

    def test_backstage_pass(self):
        # Case 1: sell_in > 10
        item = BackstagePass("Backstage Pass", 11, 10)
        item.update()
        self.assertEqual(item.quality, 11)  # Should increase by 1
        self.assertEqual(item.sell_in, 10)

        # Case 2: 5 < sell_in ≤ 10
        item = BackstagePass("Backstage Pass", 10, 10)
        item.update()
        self.assertEqual(item.quality, 12)  # Should increase by 2
        self.assertEqual(item.sell_in, 9)

        # Case 3: 0 < sell_in ≤ 5
        item = BackstagePass("Backstage Pass", 5, 10)
        item.update()
        self.assertEqual(item.quality, 13)  # Should increase by 3
        self.assertEqual(item.sell_in, 4)

        # Case 4: sell_in = 0 (concert starts, quality drops to 0)
        item = BackstagePass("Backstage Pass", 0, 10)
        item.update()
        self.assertEqual(item.quality, 0)  # Quality should drop to 0
        self.assertEqual(item.sell_in, -1)

        # Case 5: Quality should never exceed 50
        item = BackstagePass("Backstage Pass", 5, 49)
        item.update()
        self.assertEqual(item.quality, 50)  # Max quality limit
        self.assertEqual(item.sell_in, 4)


if __name__ == '__main__':
    unittest.main()
