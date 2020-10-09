# !/usr/bin/env python
# -*- coding:Utf8 -*-
# # pygame import
from items import Item
# import random
# pygame initialization


class Guardian(Item):     # with sprite method
    def __init__(self, name, image, x, y, type):
        Item.__init__(self, name, image, x, y)
        self.type=type
