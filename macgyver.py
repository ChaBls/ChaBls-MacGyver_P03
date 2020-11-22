# !/usr/bin/env python
# -*- coding:Utf8 -*-
from constantes import *


class MacGyver:
    def __init__(self, x=0, y=0, inventory=[]):
        self.x=x
        self.y=y
        self.inventory=inventory

    def direction(self):

        """This method allows the player to chose MacGyver direction.
        Everytime the player asks for a specific direction, MacGyver coordinates
        are accordingly changing.
        If requested coordinates correspond to a wall, the demand is denied in order
        to avoid any collision. The player is automatically notified and has to type
        another choice.
        """

        direc_key = input("R(right), L(left), D(down), U:(up) : ")
        if direc_key == 'R':
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
            if self.y == 0:
                print("Access denied")
            else:
                self.y-=1
                return self.y

    def caught_item(self):

        """Method will print sentences everytime MacGyver
        caught an item, and then kill the corresponding item.
        The player will know how many items still have to be grabbed.
        """

        pass

    def guardian_interaction(self):

        """This method determines what occurs
        if MacGyver(player) arrives in front of the guardian
        will all the items, or only a with a part of them.
        """

        pass
