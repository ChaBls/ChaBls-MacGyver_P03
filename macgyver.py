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
        self.score_update = 0

    def go_right(self,walls):
        """The 4 following methods determine what "right", "left", "down"
        and "up" directions are. Meanwhile, collisions are also managed :
        if player coordinates are matching with walls or border ones,
        player x and y axis return to their previous position.
        """

        self.x+=1
        if self.x>=column_number:
            self.x-=1
            return self.x
        elif (self.y,self.x) in walls:
            self.x-=1
            return self.x
        else:
            return self.x

    def go_left(self,walls):
        self.x-=1
        if self.x<=0:
            self.x+=1
            return self.x
        elif (self.y,self.x) in walls:
            self.x+=1
            return self.x
        else:
            return self.x

    def go_down(self,walls):        
        self.y+=1
        if self.y>=row_number:
            self.y-=1
            return self.y
        elif (self.y,self.x) in walls:
            self.y-=1
            return self.y
        else:
            return self.y

    def go_up(self,walls):
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
        caught an item, and then kills (removes) the corresponding item.
        The player know continuously how many items still have to be grabbed.
        """
    
        if (self.y,self.x) in floor:
            artifact=False
            for loot in item_object:
                if (self.y,self.x) == (loot.y,loot.x):
                    artifact=True
                    if loot.name == 'swiss knife':
                        item_object.remove(loot)
                        print("Do you really need a {}...?".format(loot.name))
                        return (self.y,self.x)
                    elif loot.name == 'mushroom':
                        item_object.remove(loot)
                        print("Don't eat this... too late ?!")
                        return (self.y,self.x)
                    else:
                        self.score_update+=1
                        self.inventory.append(loot)
                        item_object.remove(loot)
                        print("You caught {}".format(loot.name))
                        return (self.y,self.x)
            if artifact==False:
                pass

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
                self.winner="YEEES!! Mac Gyver put his {}".format(guardian.type),"down!\n","YOU WON!"
                quit()
            else:
                self.loser="You don't have all the items... you lose!"
                quit()
        elif ennemy==False:
            pass
