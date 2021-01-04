# !/usr/bin/env python
# -*- coding:Utf8 -*-
from constantes import row_number
from constantes import column_number
from constantes import white
from guardian import Guardian
import game
import pygame
import time
pygame.init()


# Determine what the score font will be and its size
main_font = pygame.font.SysFont("arial",20)

class MacGyver:
    def __init__(self,image=None,x=0,y=0,inventory=[]):
        self.x=x
        self.y=y
        self.inventory=inventory
        self.image=image
        self.rect=self.image.get_rect()
        self.score_update = 0


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
                    if self.x>=column_number:
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
                    if self.y>=row_number:
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

            # Quit the game, if the player clic on window exit cross
            elif event.type == pygame.QUIT:
                quit()

    def caught_item(self,floor,item_object,screen):
        """Method will print sentences everytime MacGyver
        caught an item, and then kills (removes) the corresponding item.
        The player know continuously how many items still have to be grabbed.
        """

        if (self.y,self.x) in floor:
            artifact=False
            for loot in item_object:
                if (self.y,self.x) == (loot.y,loot.x):
                    artifact=True
                    if loot.name == 'mushroom':
                        item_object.remove(loot)
                        return (self.y,self.x)
                    else:
                        self.score_update+=1
                        self.inventory.append(loot)
                        item_object.remove(loot)
                        return (self.y,self.x)
            if artifact==False:
                pass

    def guardian_interaction(self,guardian,floor,item_object,background):

        """This method determines what occurs if MacGyver(player) arrives
        in front of the guardian with only a part of the items (in this case,
        a message is printed, the game is over and stop) or all of them (in this case,
        a mesage is printed, player wins and the game is over)
        """

        ennemy=False
        if (self.y,self.x) == (guardian.y,guardian.x):
            ennemy=True
            if len(self.inventory)==3:
                winner_sentence="'YEEES!! Mac Gyver put his ennemy down!\n', 'YOU WON!'"
                winner = main_font.render((winner_sentence),True,white)
                background.blit(winner,(coor_main_TextX,coor_main_TextY))
                quit()
            else:
                loser_sentence="You don't have all the items... you lose!"
                loser = main_font.render((loser_sentence),True,white)
                for i in range(1):
                    background.blit(loser,(coor_main_TextX,coor_main_TextY))
                quit()
        elif ennemy==False:
            pass

