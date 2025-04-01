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
