# !/usr/bin/env python
# -*- coding:Utf8 -*-

""" 'colum_number' and 'row_number' are
used to determine labyrinth borders
"""
column_number = 14
row_number = 14

# Size of each image used into the game (40x40)
sprite_height = 40
sprite_width = 40

# score text coordinates
coor_score_TextX = 390
coor_score_TextY = 605

# 'Game Over' text coordinates
coor_main_textX = 20
coor_main_textY = 612

# Place where 'Game Over' text is displayed
display_width = 300
display_height = 300

# Text color
white = (255,255,255)

# List of 3 dictionnaries, used in 'game.py'
item_list= [
    {'name':'ether','image': "Entities/assets/ether.png",'drug':False},
    {'name':'needle','image': "Entities/assets/aiguille.png",'drug':False},
    {'name':'plastic tube','image': "Entities/assets/tube_plastique.png",'drug':False},
    {'name':'mushroom','image':"Entities/assets/mushroom.png",'drug':True}
]