# !/usr/bin/env python
# -*- coding:Utf8 -*-
from game import Game   # Import the "Game" class from "game.py"
from macgyver import MacGyver
import random
from random import randint
from constantes import *


def main():     # Called if the file is imported as a module
    labyrinth = Game()
    labyrinth.labyrinth_reading()
    labyrinth.labyrinth_printing()


# Player object
player=MacGyver()

# x and y are randomly generated when the game starts
player.x=random.randint(0,14)
player.y=random.randint(0,14)

running=True

while running:
    player.direction()


if __name__ == "__main__":  # Call "main()" if we run the file directly (not as a module)
    main()