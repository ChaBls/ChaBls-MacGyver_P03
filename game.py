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
        pass

    def labyrinth_reading(self):
        self.walls = []

        file = open("labyrinth.txt", "r").readlines()
        for indexLine, line in enumerate(file):
            for indexCharacter, character in enumerate(line):
                if character == "M":
                    self.walls.append(indexCharacter, indexLine)
                elif character == "G":
                    self.guardian =  Guardian(x=indexCharacter, y=indexLine)
                elif character == "P":
                    self.player = MacGyver(x=indexCharacter, y=indexLine)

    def labyrinth_printing(self):
        for i in range(14):
            for j in range(14):
                if (i, j) in self.walls:
                    print("M")
                elif self.player.x == i and self.player.y == j:
                    print("P")
                elif self.guardian.x == i and self.guardian.y == j:
                    print("G")
                else:
                    print(" ")
