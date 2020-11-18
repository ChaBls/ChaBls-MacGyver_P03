# !/usr/bin/env python
# -*- coding:Utf8 -*-
from macgyver import MacGyver
from guardian import Guardian


class Game:
    def lab_reading(self):
        self.walls=[]

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
                    self.guardian = Guardian(type="ennemy", x=coorLetter, y=coorLine)
                elif letter == 'P':
                    self.player = MacGyver(x=coorLetter, y=coorLine)

    def lab_printing(self):
        
        """For i position between 0 and 14 and j position between 0 and 14 : compare 
        these positions to player, guardian and walls coordinates. According to the
        result, print the appropriate letter (M for walls, P for player or G for
        guardian
        """

        for i in range(14):
            for j in range(14):
                if (i,j) in self.walls:
                    print('M', end="")
                    # Print 'M' and removes all characters/signs placed after it

                elif i == self.player.x and j == self.player.y:
                    print('P', end="")
                elif i == self.guardian.x and j == self.guardian.y:
                    print('G', end="")
                else:
                    print(" ", end="")
            print("\n")         
            # New line
