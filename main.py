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

black = (0,0,0)
white = (255,255,255)

pygame.display.set_caption("MACGYVER QUEST")
screen = pygame.display.set_mode((650,650))
background = pygame.image.load("assets/black_wallpaper.jpg").convert_alpha()
screen_size = screen.get_height() * screen.get_width()
screen.fill(white)

labyrinth.lab_reading()

running=True

while running:
    labyrinth.lab_printing(screen,background)
    screen.blit(background,screen_size)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                quit()
            else:
                labyrinth.player.direction(labyrinth.walls,event.key)
                labyrinth.player.caught_item(labyrinth.floor,labyrinth.item_object)
                labyrinth.player.inventory_update()
                labyrinth.player.guardian_interaction(labyrinth.guardian,labyrinth.floor,labyrinth.item_object)
    
    pygame.display.update()

