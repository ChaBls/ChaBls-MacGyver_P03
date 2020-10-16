# !/usr/bin/env python
# -*- coding:Utf8 -*- 
import random


class Item:
    """ In this class, I created an instance of
     self as an object, with name, image, x and y as attributes."""
    def __init__(self, x, y):
        self.x=x
        self.y=y

""" New objects are created, from Item. For each of them, I configure their own
attributes. x and y are randomly generated"""
ether = Item(x=random.randint(0, 14), y=random.randint(0, 14))  # random integer in range (0, 14)
needle = Item(x=random.randint(0, 14), y=random.randint(0, 14))
plastic_tube = Item(x=random.randint(0, 14), y=random.randint(0, 14))
