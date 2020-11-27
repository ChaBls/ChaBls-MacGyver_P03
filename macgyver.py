# !/usr/bin/env python
# -*- coding:Utf8 -*-
from constantes import *
import game


class MacGyver:
    def __init__(self, x=0, y=0, inventory=[],position=[]):
        self.x=x
        self.y=y
        self.inventory=inventory
        self.position=position

    def direction(self,walls,floor,loot,item_dict,item_object):
    
        """This method allows the player to chose MacGyver direction.
        Everytime the player asks for a specific direction, MacGyver coordinates
        are accordingly changing.
        If requested coordinates correspond to a wall, the demand is denied in order
        to avoid any collision. The player is automatically notified and has to type
        another choice.
        """

        direc_key = input("R(right), L(left), D(down), U:(up) : ")
        if direc_key=='R':
            self.x+=1
        if self.x >= column_number:
            print("You are off-limits!")
        elif self.position in walls:                
            print("You can't go through the walls...")
        elif self.position in floor:
            return self.position
        else:
            for key, value in item_dict:
                if value == self.position:
                    self.inventory.append(item_dict[value])
                    item_object.remove(loot)
                    return self.position
        if direc_key=='L':
            if self.position in floor:
                self.x-=1
                return self.position
            elif self.x == 0:
                print("Access denied")
                return self.position
            elif self.position in walls:
                print("Access denied")
                return self.position
            else:
                for key, value in item_dict:
                    if value == self.position:
                        self.x-=1
                        self.inventory.append(item_dict[value])
                        item_object.remove(loot)
                        return self.position
        if direc_key == 'D':
            if self.position in floor:
                self.y+=1
                return self.position
            elif self.y==row_number:
                print("Access denied")
                return self.position
            elif self.position in walls:
                print("Access denied")
                return self.position
            else:
                for key, value in item_dict:
                    if value == self.position:
                        self.y+=1
                        self.inventory.append(item_dict[value])
                        item_object.remove(loot)
                        return self.position
        if direc_key == 'U':
            if self.position in floor:
                self.y-=1
                return self.position
            elif self.y== 0:
                print("Access denied")
                return self.position
            elif self.position in walls:
                print("Access denied")
                return self.position
            else:
                for key, value in item_dict:
                    if value == self.position:
                        self.x-=1
                        self.inventory.append(item_dict[value])
                        item_object.remove(loot)
                        return self.position

    def where_is_macgyver(self):
        self.position.append((self.y,self.x))


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
