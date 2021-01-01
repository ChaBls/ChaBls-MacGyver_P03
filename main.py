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
from constantes import coorTextX
from constantes import coorTextY

pygame.init()


# Create an object of Game class
labyrinth = Game()

# Initialize the window
screen = pygame.display.set_mode((600,600))

# Get the rectangular area of the surface
screen_rect = screen.get_rect()

# Create a background with a specific image
background = pygame.image.load("assets/black_wallpaper.jpg").convert()

# Determine what the score font will be and its size
score_font = pygame.font.SysFont("arial",32)

# Read labyrinth.txt file, calling 'Game' method
labyrinth.lab_reading()

# Put a name on top the window screen
pygame.display.set_caption("MACGYVER QUEST")


over = False

# Game is running into this loop
while not over:

    # Appply background to the screen, with screen surface as a reference for the position
    screen.blit(background,screen_rect)
    
    # Print labyrinth, calling 'Game' method
    labyrinth.lab_printing(background,sprite_width,sprite_height)

    # Initialize game icon
    pygame.display.set_icon(labyrinth.icon_img)

    # Initialize score text and display it
    score = score_font.render("Inventory:" + str(labyrinth.player.score_update),True,white)
    background.blit(score,(coorTextX,coorTextY))

    # Do something, according to event
    for event in pygame.event.get(): 

        # The player can close the screen manually or chose a direction      
        if event.type == pygame.QUIT:   # If the player clic on window exit cross
            over = True

        # Call player direction method, accordingly to pressed direction arrow
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                labyrinth.player.go_right(labyrinth.walls)
            elif event.key == pygame.K_LEFT:
                labyrinth.player.go_left(labyrinth.walls)
            elif event.key == pygame.K_DOWN:
                labyrinth.player.go_down(labyrinth.walls)
            elif event.key == pygame.K_UP:
                labyrinth.player.go_up(labyrinth.walls)

            # The player can close the screen by pressing 'ECHAP'  
            elif event.key == pygame.K_ESCAPE:
                over = True

            # Call player methods    
            labyrinth.player.caught_item(labyrinth.floor,labyrinth.item_object)
            labyrinth.player.guardian_interaction(labyrinth.guardian,labyrinth.floor,labyrinth.item_object)

    # update the display
    pygame.display.flip()

