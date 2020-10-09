# !/usr/bin/env python
# -*- coding:Utf8 -*-
# pygame import
from items import Item
from macgyver import MacGyver
from guardian import Guardian
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

with open("labyrinth.txt", "r") as f:
    for column in range(14):
        if f[column] is M:
            walls.append((%line, column))
        elif f[column] is G:
            guardian =  Guardian(name="Mr Turner", image="assets/Gardien.png", type="your enemy", x=14, y=1)
        elif f[column] is P:
            player = MacGyver(name="Mac Gyver", type="heroe", image="assets/MacGyver.png", velocity=2, score=str, over=False, x=1, y=1)

    for i in range(14):
        for j in range (14):
            if element in walls:
                print('M')
            elif player.rect.x = i and player.rect.y = j:
                print('P')
