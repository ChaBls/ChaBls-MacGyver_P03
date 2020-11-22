# !/usr/bin/env python
# -*- coding:Utf8 -*-
from macgyver import MacGyver
from guardian import Guardian
from items import Item


class Game:
    def __init__(self):
        self.walls=[]

    def lab_reading(self):
        file = open("labyrinth.txt", "r").readlines()
        # Open labyrinth file and save it in the variable 'file'
        
        for coorLine, line in enumerate(file):
        # Get line coordinates (from file), save it in coorLine

            for coorLetter, letter in enumerate(line):
            # Get letter coordinates (from line), save it in coorLetter

                """If the letter corresponds to 'M', we will add its position to walls list
                If the letter corresponds to 'P' or 'G', we'll create player
                or guardian objects, with their own position
                """

                if letter == 'M':
                    self.walls.append((coorLine, coorLetter))
                elif letter == 'G':
                    self.guardian=Guardian(type="ennemy", x=coorLetter, y=coorLine)
                elif letter == 'P':
                    self.player=MacGyver(x=coorLetter, y=coorLine)

    def lab_printing(self, item_list):

        """Line from 0 to 14 and column from 0 to 14 : the method analyze each
        character position to player, guardian and walls coordinates. According to
        the result, the method print the appropriate letter ('M' for walls,
        'P' for player or 'G' for guardian).
        The method also browse list of items created in 'constantes' file.
        Random coordinates are chosen for each item, corresponding
        letter will be printed into the labyrinth.
        To compare walls/guardian/player positions with items ones avoid
        collisions: items can pop only where there is available space.
        """

        for i in range(14):
            for j in range(14):
                if (i,j) in self.walls:
                    print('M', end="")
                    # Print 'M' and removes all characters/signs placed after it
                    
                elif j==self.player.x and i==self.player.y:
                    print('P', end="")
                elif j==self.guardian.x and i==self.guardian.y:
                    print('G', end="")   
                else:
                    for item in item_list:
                        if j==ether.x and i==ether.y:
                            print('E', end="")
                        if j==needle.x and i==needle.y:
                            print('N', end="")
                        if j==plastic_tube.x and i==plastic_tube.y:
                            print('T', end="")
                    print(" ", end="")
            print("\n")         
            # New line
