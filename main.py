# !/usr/bin/env python
# -*- coding:Utf8 -*-
from game import Game
from macgyver import MacGyver
from constantes import *


# Objects
labyrinth = Game()
mac_gyver = MacGyver()

walls = labyrinth.walls
item_dict = labyrinth.item_dict
item_object = labyrinth.item_object
floor = labyrinth.floor
loot = labyrinth.loot
position = mac_gyver.position

# Method
labyrinth.lab_reading()
labyrinth.player.where_is_macgyver()

# Loop
running=True

"""The method 'direction()' is called while the game is running.
The player can now chose MacGyver direction continually.
Updated labyrinth is printed after each direction change.
"""

while running:
    labyrinth.lab_printing(position)
    labyrinth.player.direction(walls,floor,loot,item_dict,item_object)
    labyrinth.player.where_is_macgyver()
