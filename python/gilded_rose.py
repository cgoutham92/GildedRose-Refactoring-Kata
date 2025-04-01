# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"

    def update(self):
        raise NotImplementedError("Update method must be implemented in subclasses")


class DefaultItem(Item):

    def update(self):
        self.sell_in -= 1
        self.quality = max(0, self.quality - (2 if self.sell_in < 0 else 1))


class AgedBrie(Item):
    def update(self):
        self.sell_in -= 1
        self.quality = min(50, self.quality + (2 if self.sell_in < 0 else 1))


class BackstagePass(Item):
    def update(self):
        if self.sell_in <= 0:
            self.quality = 0
        else:
            increase = 3 if self.sell_in <= 5 else 2 if self.sell_in <= 10 else 1
            self.quality = min(50, self.quality + increase)
        self.sell_in -= 1


class Sulfuras(Item):
    def update(self):
        pass  # Ensures quality remains constant and sell_in never changes


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if isinstance(item, Item):
                item.update()


if __name__ == '__main__':
    items = [
        DefaultItem("foo", 1, 10),
        AgedBrie("Aged Brie", 1, 10),
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", 11, 10),
        Sulfuras("Sulfuras, Hand of Ragnaros", 5, 80),
    ]

    gilded_rose = GildedRose(items)

    print("Before Update:")
    for item in items:
        print(item)

    gilded_rose.update_quality()

    print("\nAfter Update:")
    for item in items:
        print(item)
