# pygame import
from items import Item
from labyrinth import *
# from macgyver import MacGyver
# from guardian import Guardian
# from constantes import *
# pygame initialization

# display screen, with width and height defined in constantes.py
# display player, guardian, items and inventory


class Game:
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.running = True

# open and read "labyrinth.py" file
fic = open("labyrinth.py", "r")
print(lab)
fic.close()
