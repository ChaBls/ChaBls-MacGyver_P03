# !/usr/bin/env python
# -*- coding:Utf8 -*-
from Config.constantes import ROW_NUMBER
from Config.constantes import COLUMN_NUMBER
from Config.constantes import WHITE
from Config.constantes import COOR_MAIN_TEXTX
from Config.constantes import COOR_MAIN_TEXTY
from Entities.guardian import Guardian
import Entities.game
import pygame
import time

pygame.init()

# Determines what the score font and its size will be and save it
main_font = pygame.font.SysFont("arial",20)


class MacGyver:

    def __init__(self,image=None,x=0,y=0,inventory=[],over=False,high=False):
        self.x=x
        self.y=y
        self.inventory=inventory
        self.image=image
        self.rect=self.image.get_rect()
        self.score_update = 0
        self.over=over
        self.high=high


    def direction(self,walls):
        """The following methods determine what "right", "left", "down"
        and "up" directions are. Meanwhile, collisions are also managed :
        if player coordinates are matching with walls or border ones,
        player x and y axis return to their previous position.
        """

        # Do something, according to event
        for event in pygame.event.get():

            # If the player press any keyboard key
            if event.type == pygame.KEYDOWN:

                # If the pressed key is right direction arrow
                if event.key == pygame.K_RIGHT:
                    self.x+=1
                    if self.x>=COLUMN_NUMBER:
                        self.x-=1
                        return self.x
                    elif (self.y,self.x) in walls:
                        self.x-=1
                        return self.x
                    else:
                        return self.x

                elif event.key == pygame.K_LEFT:
                    self.x-=1
                    if self.x<=0:
                        self.x+=1
                        return self.x
                    elif (self.y,self.x) in walls:
                        self.x+=1
                        return self.x
                    else:
                        return self.x

                elif event.key == pygame.K_DOWN:
                    self.y+=1
                    if self.y>=ROW_NUMBER:
                        self.y-=1
                        return self.y
                    elif (self.y,self.x) in walls:
                        self.y-=1
                        return self.y
                    else:
                        return self.y

                elif event.key == pygame.K_UP:
                    self.y-=1
                    if self.y<=0:
                        self.y+=1
                    elif (self.y,self.x) in walls:
                        self.y+=1
                        return self.y
                    else:
                        return self.y

                # The player can close the screen by pressing 'ECHAP'  
                elif event.key == pygame.K_ESCAPE:
                    quit()

            # Quit the game, if the player clic on the window exit cross
            elif event.type == pygame.QUIT:
                quit()

    def caught_item(self,floor,item_object):
        """The following method will allow MacGyver to 'take' the items:
        if MacGyver is placed on an item, 'artifact' boolean becomes 'True';
        and the item is automatically removed from 'item_object' list
        (game attribute, where we first created all the items).
        The image of the caught item will no longer be displayed by 'lab_printing',
        as its not exsting anymore in 'item_object'.

        If 'drug' boolean is 'True', player attribute 'high' is 'True'.
        The item is not saved into player's inventory.

        If 'drug' boolean is 'False', the item is placed into player's inventory,
        player 'score_update' attribute is incremented (+1); player attribute 'high'
        remains unchanged.

        The player knows continuously how many items have been caught already.
        """

        if (self.y,self.x) in floor:
            artifact=False
            for loot in item_object:
                if (self.y,self.x) == (loot.y,loot.x):
                    artifact=True
                    item_object.remove(loot)
                    if loot.drug == True:
                        self.high=True
                    else:
                        self.score_update+=1
                        self.inventory.append(loot)
        return item_object

    def guardian_interaction(self,guardian,floor,item_object,screen):

        """'ennemy' boolean becomes 'True' as soon as MacGyver meets the guardian.
        
        This method determines what occurs if MacGyver arrives
        in front of the guardian with only a part of the required items:
        a message is printed in order to inform the player that the game is over
        and the screen is freezed.

        If he's got all the required items
        ('score_update' attribute has been incremented by 3):
        the window closes automatically, player won.
        """

        ennemy=False
        if (self.y,self.x) == (guardian.y,guardian.x):
            ennemy=True
            if self.score_update == 3:
                quit()
            else:
                self.over=True
                loser_sentence="GAME OVER,YOU'RE DEAD"
                loser = main_font.render((loser_sentence),True,WHITE)
                screen.blit(loser,(COOR_MAIN_TEXTX,COOR_MAIN_TEXTY))
        elif ennemy==False:
            pass

