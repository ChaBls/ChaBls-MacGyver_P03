# !/usr/bin/env python
# -*- coding:Utf8 -*-
from constantes import *


class MacGyver:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def direction(self):
        direc_key = input("R:right, L:left, D:down, U:up")
        if direc_key == 'R'':
            if self.x == column_number:
                print("Access denied")
            else:
                self.x+=1
                return self.x
        if direc_key == 'L':
            if self.x == 0:
                print("Access denied")
            else:
                self.x-=1
                return self.x
        if direc_key == 'D':
            if self.y == row_number:
                print("Access denied")
            else:
                self.y+=1
                return self.y
        if direc_key == 'U':
            if selx.y == 0:
                print("Access denied")
            else:
                self.y-=1
                return self.y


    def direction_update(self):
        '''For each given keyboard key, a direction will be assigned.'''

    def caught_item(self):
        '''I will print sentences evrytime MacGyver(player)
        caught an item, and then kill this item.
        I'd like to know how many items still have to be grabbed.'''
        pass

    def guardian_interaction(self):
        '''This method determines what occurs
        if MacGyver(player) arrives in front of the guardian
        will all the items, or only a with a part of them.'''
        pass
