# !/usr/bin/env python
# -*- coding:Utf8 -*- 
# pygame import
# import random
# from constantes import *
# Pygame initialization

# items_group = sprite

class Item:  # with sprite module
    """ In this class, I created an instance of
     self as an object, with name and image as attributes."""
    def __init__(self, name, image, x, y):
        self.name=name
        self.image=image
        # self.rect=rect with pygame
        self.x=x
        self.y=y

# rect still has to be configured with pygame.
""" New objects are created. For each of them, I configure their own
version of Items attributes. """
ether = Item(name="ether", image="assets/ether.png")
needle = Item("needle", "assets/aiguille.png")
plastic_tube = Item("plastic tube", "assets/tube_plastique.png")
# items_group.add(ether, needle, plastic_tube)

if __name__ == "__main__":
    """ I print attributes, only if items.py is called """
    print(ether.name)
    print(needle.image)
