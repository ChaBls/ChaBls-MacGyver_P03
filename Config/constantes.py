# !/usr/bin/env python
# -*- coding:Utf8 -*-

""" 'colum_number' and 'row_number' are
used to determine labyrinth borders
"""
COLUMN_NUMBER = 14
ROW_NUMBER = 14

# Size of each image used into the game (40x40)
SPRITE_HEIGHT = 40
SPRITE_WIDTH = 40

# score text coordinates
COOR_SCORE_TEXTX = 390
COOR_SCORE_TEXTY = 605

# 'Game Over' text coordinates
COOR_MAIN_TEXTX = 20
COOR_MAIN_TEXTY = 612

# Text color
WHITE = (255,255,255)

# List of 3 dictionnaries, used in 'game.py'
ITEM_LIST= [
    {'name':'ether','image': "Entities/assets/ether.png",'drug':False},
    {'name':'needle','image': "Entities/assets/aiguille.png",'drug':False},
    {'name':'plastic tube','image': "Entities/assets/tube_plastique.png",'drug':False},
    {'name':'mushroom','image':"Entities/assets/mushroom.png",'drug':True}
]