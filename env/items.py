# pygame import
# import random
# from constantes import *
# Pygame initialization

# items_group = sprite

class Item:  # with sprite module
    def __init__(self, name, image):
        self.name = name
        self.image = image
        # self.rect = rect with pygame
        # self.rect.x = rect.x with pygame
        # self.rect.y = rect.y with pygame

# rect, rect.x, rect.y has to be configured with pygame
ether = Item("ether", "assets/ether.png")
needle = Item("needle", "assets/aiguille.png")
plastic_tube = Item("plastic tube", "assets/tube_plastique.png")
# items_group.add(ether, needle, plastic_tube)

print(ether.name)
print(needle.image)
