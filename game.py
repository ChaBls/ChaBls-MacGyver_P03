# !/usr/bin/env python
# -*- coding:Utf8 -*-
# pygame import
from items import Item
# from macgyver import MacGyver
# from guardian import Guardian
# from constantes import *
# pygame initialization

# display screen, with width and height defined in constantes.py
# display player, guardian, items and inventory


class Game:
    def __init__(self, color, name):
        self.color=color
        self.name=name
        self.running=True

line = 0
walls = []
wall = walls.append

with open("labyrinth.txt", "r") as f:
    for column in range(14):
        if f[column] is M:
            wall((%line, column))
        elif f[column] is G:
            G = guardian
        elif f[column] is P:
            P = player

    for i in range(14):
        for j in range (14):
            if wall in walls:
                print('M')
            elif player.rect.x = i and player.rect.y = j:
                print('P')
