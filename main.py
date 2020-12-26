# !/usr/bin/env python
# -*- coding:Utf8 -*-
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import sys
import pygame
from game import Game
from macgyver import MacGyver
pygame.init()


"""The method 'direction()' is called while the game is running.
The player can now chose MacGyver direction continually.
Updated labyrinth is printed after each direction change.
"""

labyrinth = Game()

labyrinth.lab_reading()

floor = labyrinth.floor
walls = labyrinth.walls
item_object = labyrinth.item_object
guardian = labyrinth.guardian

running=True

while running:
    labyrinth.lab_printing()
    labyrinth.player.direction(walls,event.key)
    labyrinth.player.caught_item(floor,item_object)
    labyrinth.player.inventory_update()
    labyrinth.player.guardian_interaction(guardian,floor,item_object)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
            else:
                labyrinth.player.direction(walls,event.key)
