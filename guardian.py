# !/usr/bin/env python
# -*- coding:Utf8 -*-
from items import Item


class Guardian(Item):
    def __init__(self, x, y, type):
        Item.__init__(self, x, y)
        self.type=type
