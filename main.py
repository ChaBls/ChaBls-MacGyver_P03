# !/usr/bin/env python
# -*- coding:Utf8 -*-
from game import Game
from macgyver import MacGyver
from items import Item
from constantes import *
import random
from random import randint


# Objects
labyrinth = Game()

ether=item_list.append(Item(x=random.randint(0,14),y=random.randint(0,14)))
needle=item_list.append(Item(x=random.randint(0,14),y=random.randint(0,14)))
plastic_tube=item_list.append(Item(x=random.randint(0,14),y=random.randint(0,14)))

# Methods
labyrinth.lab_reading()
labyrinth.lab_printing(item_list)

# Loop
running=True

"""The method 'direction()' is called while the game is running.
The player can now chose MacGyver direction continually.
Updated labyrinth is printed after each direction change.
"""

while running:
    labyrinth.player.direction()
    labyrinth.lab_printing(item_list)
    continue
