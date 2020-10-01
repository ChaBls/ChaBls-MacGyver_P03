# !/usr/bin/env python
# -*- coding: utf-8 -*- 
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
        self.color = color
        self.name = name
        self.running = True

i = 0
# open and read "labyrinth.txt" file as "f"
with open("labyrinth.txt", "r") as f:
    my_list = [tuple(map(str, i.split(','))) for i in f]   # split each line with ","
    # create a list of iterable objects with map() method, from the open file
    for line in f:
        for i in line:
            if i == 'M':
                print("assets/prisma.jpg")
                continue
        pass
    i += 1
print(f)
