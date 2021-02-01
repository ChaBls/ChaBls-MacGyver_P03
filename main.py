#!/usr/bin/env python
# -*- coding:Utf8 -*-
"""'shebang line' allows the intepreter to use the right
version of Python, according to the virtual environment.
Universal encoding is setted with the second line.
"""
import os
import sys
import pygame
from Entities.game import Game
from Entities.macgyver import MacGyver
from Config.constantes import SPRITE_WIDTH
from Config.constantes import SPRITE_HEIGHT
from Config.constantes import WHITE
from Config.constantes import COOR_SCORE_TEXTX
from Config.constantes import COOR_SCORE_TEXTY

# Initialize Pygame
pygame.init()

# Create an object of Game class
labyrinth = Game()
# Save in the variable 'screen' the window frame display
screen = pygame.display.set_mode((600,650))
# Get the rectangular area of the surface
screen_rect = screen.get_rect()
# Create a background with a specific image
background = pygame.image.load("Entities/assets/black_wallpaper.jpg").convert()
# Determine what the score font will be and its size
score_font = pygame.font.SysFont("arial",32)

# Read labyrinth.txt file, calling 'Game' method
labyrinth.lab_reading()

# Put a name on top the window screen and load the icon
pygame.display.set_caption("MACGYVER QUEST")
icon_img=pygame.image.load("Entities/assets/icone.png")

running = True

# Loop
while running:

    """Appply background to the screen, with screen surface 'screen_rect' 
    as a reference for the position
    """
    screen.blit(background,screen_rect)
    
    # Print labyrinth, calling 'Game' method
    labyrinth.lab_printing(background,SPRITE_WIDTH,SPRITE_HEIGHT)

    # Display game icon
    pygame.display.set_icon(icon_img)

    """Initialize score text parameters
    pygame.font.render parameters = (text, antialias, color, background)
    antialias is a boolean : if 'True', characters are smoothered
    """
    score = score_font.render("Inventory : " + str(labyrinth.player.score_update),True,WHITE)
    # Display score text, with (X,Y) configured into 'constantes' file
    screen.blit(score,(COOR_SCORE_TEXTX,COOR_SCORE_TEXTY))

    # Call player methods    
    labyrinth.item_object=labyrinth.player.caught_item(labyrinth.floor,labyrinth.item_object)
    labyrinth.player.guardian_interaction(labyrinth.guardian,labyrinth.floor,labyrinth.item_object,screen)

    """While boolean player attribute 'over' is 'False', 'direction()' method
    is called continuously. If 'over' is True, according to 
    'guardian_interaction()' method, it means that MacGyver met the guardian,
    without having all the required items in his inventory. Game is freezed,
    'direction()' method will no longer be called.
    """

    if labyrinth.player.over == False:
        labyrinth.player.direction(labyrinth.walls) 
    else:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
                else:
                    pass
            elif event.type == pygame.QUIT:
                running=False

    # Update the entiere screen at the end of the loop
    pygame.display.flip()

