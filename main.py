# !/usr/bin/env python
# -*- coding:Utf8 -*-
from game import Game
from macgyver import MacGyver
from constantes import *


# Loop
running=True

"""The method 'direction()' is called while the game is running.
The player can now chose MacGyver direction continually.
Updated labyrinth is printed after each direction change.
"""

print("Mac Gyver was sent on a perilous mission and, as he was about\n"
"to discover important secrets, he was suddenly interrupted, finding\n"
"himself LOCKED IN A MAZE!\n"
"Of course, he knows how to make a syringe from nothing...\n"
"Here is the list of all the items you need to find :\n"
"1- ether bottle\n"
"2- sharp needle\n"
"3- thin plastic tube\n"
"LET'S GO!")

labyrinth = Game()

labyrinth.lab_reading()

walls = labyrinth.walls
item_dict = labyrinth.item_dict
item_object = labyrinth.item_object
floor = labyrinth.floor
guardian = labyrinth.guardian

while running:        
    labyrinth.lab_printing()
    labyrinth.player.direction(walls)
    labyrinth.player.caught_item(floor,item_object)
    labyrinth.player.inventory_update()
    labyrinth.player.guardian_interaction(guardian,floor,item_object)
