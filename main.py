# !/usr/bin/env python
# -*- coding:Utf8 -*-
from game import Game
from macgyver import MacGyver
import random
from random import randint


labyrinth = Game()

def main(self):
    # Player position is randomly generated when the game starts
    self.player.x=random.randint(0,14)
    self.player.y=random.randint(0,14)
    running=True
    while running:
        labyrinth.lab_reading()
        labyrinth.lab_printing()
        self.player.direction()
