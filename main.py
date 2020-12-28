# !/usr/bin/env python
# -*- coding:Utf8 -*-
import os
import sys
import pygame
from game import Game
from macgyver import MacGyver
from constantes import sprite_width
from constantes import sprite_height
from constantes import display_width
from constantes import display_height

pygame.init()
pygame.mixer.init()


"""The method 'direction()' is called while the game is running.
The player can now chose MacGyver direction continually.
Updated labyrinth is printed after each direction change.
"""

labyrinth = Game()  # Create an object of Game class

screen = pygame.display.set_mode((600,600)) # Initialize the window
pygame.display.set_caption("MACGYVER QUEST")    # Initialize game title
screen_rect = screen.get_rect() # Get the rectangular area of the surface
background = pygame.image.load("assets/black_wallpaper.jpg").convert()  # Create a background with a specific image

theme = "assets/MG_theme_song.wav"

labyrinth.lab_reading() # Call Game method

over = False

while not over:
    screen.blit(background,screen_rect) # Appply background to the screen, with screen surface as a reference for the position
    labyrinth.lab_printing(background,sprite_width,sprite_height)  # Call Game method
    pygame.mixer.music.load(theme)
    pygame.mixer.music.play(-1)
    for event in pygame.event.get():    # Do something, according to event
        if event.type == pygame.QUIT:   # If the player clic on window exit cross
            over = True
        elif event.type == pygame.KEYDOWN:
            event_key = event.key
            K_LEFT=pygame.K_LEFT
            K_RIGHT=pygame.K_RIGHT
            K_DOWN=pygame.K_DOWN
            K_UP=pygame.K_UP
            if event_key == pygame.K_ESCAPE:
                over = True
            else:
                labyrinth.player.direction(labyrinth.walls,event.key,pygame.K_RIGHT,pygame.K_LEFT,pygame.K_DOWN,pygame.K_UP)
                labyrinth.player.caught_item(labyrinth.floor,labyrinth.item_object)
                labyrinth.player.inventory_update()
                labyrinth.player.guardian_interaction(labyrinth.guardian,labyrinth.floor,labyrinth.item_object)
    
    pygame.display.update()

