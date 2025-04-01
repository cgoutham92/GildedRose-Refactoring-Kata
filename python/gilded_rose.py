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
