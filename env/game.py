# pygame import
from items import Item
from labyrinth import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# from macgyver import MacGyver
# from guardian import Guardian
# from constantes import *
# pygame initialization

# display screen, with width and height defined in constantes.py
# display player, guardian, items and inventory


class Game:
    def __init__(self, color, name):
        self.color = color   # frame color
        self.name = name    # frame name
        self.running = True  # maintain the frame opened

# open and read "labyrinth.py" file tuple
with open("labyrinth.py") as f:
    while True:
        M = print(mpimg.imread('assets/prisma.jpg'))
        if not M:
            print(" ")
