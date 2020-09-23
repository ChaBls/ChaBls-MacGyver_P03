# pygame import
import random
from constantes import *
# Pygame initialization


class Item:  # with sprite module
    def __init__(self, image, x, y):
        self.name = name
        self.image = image
        self.rect = rect
        self.rect.x = rect.x
        self.rect.y = rect.y

# name, image
# rect, rect.x, rect.y has to be configured with pygame
ether = Item("ether", "assets/ether.png", "None", "0", "0")
needle = Item("needle", "assets/aiguille.png", "None", "0", "0")
plastic_tube = Item("plastic tube", "assets/tube_plastique.png", "None", "0", "0")
