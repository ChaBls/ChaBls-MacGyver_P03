# !/usr/bin/env python
# -*- coding:Utf8 -*-
from constantes import row_number
from constantes import column_number
from guardian import Guardian
import game


class MacGyver:
    def __init__(self,image=None,x=0,y=0,inventory=[]):
        self.x=x
        self.y=y
        self.inventory=inventory
        self.image=image
        self.rect=self.image.get_rect()

    def direction(self,walls,event_key,K_RIGHT,K_LEFT,K_DOWN,K_UP):
        """This method allows the player to chose MacGyver direction.
        Everytime the player asks for a specific direction, MacGyver coordinates
        are accordingly changing.
        If requested coordinates correspond to a wall, the demand is denied in order
        to avoid any collision. The player is automatically notified and has to type
        another choice.
        """


        if event_key == K_RIGHT:
            self.x+=1
            if self.x>=column_number:
                self.x-=1
                return self.x
            elif (self.y,self.x) in walls:
                self.x-=1
                return self.x
            else:
                return self.x

        elif event_key == K_LEFT:
            self.x-=1
            if self.x<=0:
                self.x+=1
                return self.x
            elif (self.y,self.x) in walls:
                self.x+=1
                return self.x
            else:
                return self.x
        
        elif event_key == K_DOWN:
            self.y+=1
            if self.y>=row_number:
                self.y-=1
                return self.y
            elif (self.y,self.x) in walls:
                self.y-=1
                return self.y
            else:
                return self.y

        elif event_key == K_UP:
            self.y-=1
            if self.y<=0:
                self.y+=1
            elif (self.y,self.x) in walls:
                self.y+=1
                return self.y
            else:
                return self.y

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
                    if loot.name == 'rope':
                        print("Do you really need a {}...?".format(loot.name))
                        item_object.remove(loot)
                        return (self.y,self.x)
                    elif loot.name == 'swiss knife':
                        print("Do you really need a {}...?".format(loot.name))
                        item_object.remove(loot)
                        return (self.y,self.x)
                    else:
                        self.inventory.append(loot)
                        item_object.remove(loot)
                        print("You caught {}".format(loot.name))
                        return (self.y,self.x)
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
                quit()
            else:
                print("You don't have all the items... you lose!")
                quit()
        elif ennemy==False:
            pass
