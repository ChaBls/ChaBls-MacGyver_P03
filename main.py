# !/usr/bin/env python
# -*- coding:Utf8 -*-
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import sys
import pygame
from game import Game
from macgyver import MacGyver
from constantes import sprite_width
from constantes import sprite_height
from constantes import display_width
from constantes import display_height
from constantes import yellow
# from constantes import theme

pygame.init()
# pygame.mixer.init()


"""The method 'direction()' is called while the game is running.
The player can now chose MacGyver direction continually.
Updated labyrinth is printed after each direction change.
"""

labyrinth = Game()  # Create an object of Game class

screen = pygame.display.set_mode((600,600)) # Initialize the window
screen_rect = screen.get_rect() # Get the rectangular area of the surface
background = pygame.image.load("assets/black_wallpaper.jpg").convert()  # Create a background with a specific image
inventory_font = pygame.font.Font("assets/Starjedi.ttf",15)

labyrinth.lab_reading() # Call Game method

over = False

while not over:
    labyrinth.lab_printing(background,sprite_width,sprite_height)  # Call Game method
    pygame.display.set_caption("MACGYVER QUEST")    # Initialize game title
    pygame.display.set_icon(labyrinth.icon_img)
    screen.blit(background,screen_rect) # Appply background to the screen, with screen surface as a reference for the position
    #pygame.mixer.music.load(theme)
    #pygame.mixer.music.play(-1)
    #background.blit(labyrinth.player.inventory_update_text,(200,0))
    labyrinth.player.guardian_interaction(labyrinth.guardian,labyrinth.floor,labyrinth.item_object)
    for event in pygame.event.get():    # Do something, according to event
        if event.type == pygame.QUIT:   # If the player clic on window exit cross
            over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                labyrinth.player.go_right(labyrinth.walls)
            elif event.key == pygame.K_LEFT:
                labyrinth.player.go_left(labyrinth.walls)
            elif event.key == pygame.K_DOWN:
                labyrinth.player.go_down(labyrinth.walls)
            elif event.key == pygame.K_UP:
                labyrinth.player.go_up(labyrinth.walls)
            elif event.key == pygame.K_ESCAPE:
                over = True
            
            labyrinth.player.caught_item(labyrinth.floor,labyrinth.item_object)
            labyrinth.player.inventory_update()

            
    
    pygame.display.update()

