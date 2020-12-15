# !/usr/bin/env python
# -*- coding:Utf8 -*-
import pygame
from game import Game
from macgyver import MacGyver
pygame.init()


"""The method 'direction()' is called while the game is running.
The player can now chose MacGyver direction continually.
Updated labyrinth is printed after each direction change.
"""

black = (0,0,0)
white = (255,255,255)

window=(400,400)
screen = pygame.display.set_mode(window)
background = pygame.Surface(window)

font = pygame.font.Font("assets/Starjedi.tff", 15)

pygame.display.set_caption("MACGYVER QUEST")

# TO DO : Scroll text from the bottom to the top
print("Mac Gyver was sent on a perilous mission and, as he was about\n"
"to discover important secrets, he was suddenly interrupted, finding\n"
"himself LOCKED IN A MAZE!\n"
"Of course, he knows how to make a syringe from nothing...\n"
"Here is the list of all the items you need to find :\n"
"1- ether bottle\n"
"2- sharp needle\n"
"3- thin plastic tube\n"
"LET'S GO!")

pygame.display.update()

labyrinth = Game()

labyrinth.lab_reading()

walls = labyrinth.walls
item_dict = labyrinth.item_dict
item_object = labyrinth.item_object
floor = labyrinth.floor
guardian = labyrinth.guardian
event = pygame.event.wait()
event_key = event.key
kright = pygame.K_RIGHT
kleft = pygame.K_LEFT
kdown = pygame.K_DOWN
kup = pygame.K_UP

running=True

while running:
    labyrinth.lab_printing()
    labyrinth.player.caught_item(floor,item_object)
    labyrinth.player.inventory_update()
    labyrinth.player.guardian_interaction(guardian,floor,item_object)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
            else:
                labyrinth.player.direction(walls,event_key,kright,kleft,kdown,kup)

