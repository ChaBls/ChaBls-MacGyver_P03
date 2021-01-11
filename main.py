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
from constantes import white
from constantes import coor_score_TextX
from constantes import coor_score_TextY

pygame.init()


# Create an object of Game class
labyrinth = Game()

# Initialize the window
screen = pygame.display.set_mode((600,650))

# Get the rectangular area of the surface
screen_rect = screen.get_rect()

# Create a background with a specific image
background = pygame.image.load("assets/black_wallpaper.jpg").convert()

# Determine what the score font will be and its size
score_font = pygame.font.SysFont("arial",32)


# Read labyrinth.txt file, calling 'Game' method
labyrinth.lab_reading()

# Put a name on top the window screen and load the icon
pygame.display.set_caption("MACGYVER QUEST")
icon_img=pygame.image.load("assets/icone.png")


running = True

# Loop
while running:

    """Appply background to the screen, with screen surface 'screen_rect' 
    as a reference for the position
    """
    screen.blit(background,screen_rect)
    
    # Print labyrinth, calling 'Game' method
    labyrinth.lab_printing(background,sprite_width,sprite_height)

    # Display game icon
    pygame.display.set_icon(icon_img)

    # Initialize score text and display it
    score = score_font.render("Inventory : " + str(labyrinth.player.score_update),True,white)
    screen.blit(score,(coor_score_TextX,coor_score_TextY))

    # Call player methods    
    labyrinth.player.direction(labyrinth.walls)
    labyrinth.player.caught_item(labyrinth.floor,labyrinth.item_object,background)
    labyrinth.player.guardian_interaction(labyrinth.guardian,labyrinth.floor,labyrinth.item_object,screen)

    # Update the entiere screen
    pygame.display.flip()

