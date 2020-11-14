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
    def labyrinth_reading(self):
        self.walls = []

        file = open("labyrinth.txt", "r").readlines()
        for indexLine, line in enumerate(file):
            for indexCharacter, character in enumerate(line):
                if character == "M":
                    self.walls.append((indexCharacter, indexLine))
                elif character == "G":
                    self.guardian =  Guardian(type="your ennemy", x=indexCharacter, y=indexLine)
                elif character == "P":
                    self.player = MacGyver(x=indexCharacter, y=indexLine)

    def labyrinth_printing(self):
        for i in range(14): # For x(=line) from 0 to 14 (create a list)
            for j in range(14): # For y(=column) from 0 to 14 (create a list)
                if (i, j) in self.walls:    # If x and y are both in "self.walls" list, print "M"
                    print("M", end="")
                elif self.player.x == i and self.player.y == j: # Elif both player x and y correspond to i and j : print "P"
                    print("P", end="")
                elif self.guardian.x == i and self.guardian.y == j: # Elif both guardian x and y correspond to i and j : print "G"
                    print("G", end="")
                else:   # None of the above : print an empty space
                    print(" ", end="")
            print("\n")
