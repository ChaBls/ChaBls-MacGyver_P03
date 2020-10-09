# !/usr/bin/env python
# -*- coding:Utf8 -*-
# # pygame import
from items import Item
# import random
# pygame initialization


class Guardian(Item):     # with sprite method
    def __init__(self, name, image, type):
        Item.__init__(self, name, image)
        self.type=type

guardian = Guardian(name="Mr Turner", image="assets/Gardien.png", type="your enemy")

print(guardian.type)
