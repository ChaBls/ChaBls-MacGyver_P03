# !/usr/bin/env python
# -*- coding:Utf8 -*-
from constantes import *
from guardian import Guardian
import game


class MacGyver:
    def __init__(self,x=0,y=0,inventory=[]):
        self.x=x
        self.y=y
        self.inventory=inventory

    def direction(self,walls):
    
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
            if self.x>=column_number:
                print("Access denied")
                self.x-=1
                return self.x
            elif (self.y,self.x) in walls:
                self.x-=1
                return self.x
            else:
                return self.x
        if direc_key=='L':
            self.x-=1
            if self.x<=0:
                print("Access denied")
                self.x+=1
                return self.x
            elif (self.y,self.x) in walls:
                self.x+=1
                return self.x
            else:
                return self.x
        if direc_key == 'D':
            self.y+=1
            if self.y>=row_number:
                print("Access denied")
                self.y-=1
                return self.y
            elif (self.y,self.x) in walls:
                self.y-=1
                return self.y
            else:
                return self.y
        if direc_key == 'U':
            self.y-=1
            if self.y<=0:
                print("Access denied")
                self.y+=1
            elif (self.y,self.x) in walls:
                self.y+=1
                return self.y
            else:
                return self.y
        else:
            print("Wrong answer")

    def caught_item(self,floor,item_object):

        """Method will print sentences everytime MacGyver
        caught an item, and then kill the corresponding item.
        The player will know how many items still have to be grabbed.
        """
    
        if (self.y,self.x) in floor:
            artifact=False
            for loot in item_object:
                if (self.y,self.x) == (loot.y,loot.x):
                    artifact=True
                    self.inventory.append(loot)
                    print("You caught {}".format(loot.name))
                    item_object.remove(loot)
                    return self.x
                    return self.y
            if artifact==False:
                pass

    def inventory_update(self):

        """Player inventory is updated. This method displays
        the inventory continuously
        """

        print("*************************************")
        print("You have",len(self.inventory),"/3 items in your inventory")
        print("*************************************")

    def guardian_interaction(self,guardian,floor,item_object):

        """This method determines what occurs if MacGyver(player) arrives
        in front of the guardian with only a part of the items (in this case,
        a message is printed, the game is over and stop) or all of them (in this case,
        a mesage is printed, player wins and the game is over)
        """

        ennemy=False
        if (self.y,self.x) == (guardian.y,guardian.x):
            ennemy=True
            if len(self.inventory)==3:
                print("YEEES!! Mac Gyver put his {}".format(guardian.type),"down!\n","YOU WON!")
            else:
                print("You don't have all the items... you lose!")
                quit()
        elif ennemy==False:
            pass
