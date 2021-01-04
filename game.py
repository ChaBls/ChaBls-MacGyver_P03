# !/usr/bin/env python
# -*- coding:Utf8 -*-
import os 
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import sys
import pygame
from guardian import Guardian
from items import Item
from constantes import item_list
from macgyver import MacGyver
import random

pygame.init()


class Game:
    def __init__(self,image=None):
        # Initialize Game attributes

        # empty lists
        self.walls=[]
        self.floor=[]
        self.item_object=[]
        #empty dictionnary
        self.item_dict={}
        # empty attributes
        self.image=image


    def lab_reading(self):
        # Open labyrinth file and save it in the variable 'file'
        file = open("labyrinth.txt","r").readlines()
        
        # From 'file', get line coordinates, save it in the variable 'coorLine'
        for coorLine, line in enumerate(file):

            # From 'file', get letter coordinates, save it in the variable 'coorLetter'
            for coorLetter, letter in enumerate(line):

                """If the letter corresponds to 'M', we will add its position to 'self.walls' list

                What if the letter is 'G': we create 'guardian' object from Guardian class.
                What if the letter is 'P': we create 'player' object from MacGyver class.
                ('coorLine' and coorLetter will be used as objects coordinates)

                If none of the above, it's corresponding to floor : we add their
                coordinates to 'self.floor' list.
                """

                if letter == 'M':
                    self.walls.append((coorLine,coorLetter))
                elif letter == 'G':
                    self.guardian=Guardian(type="ennemy", x=coorLetter, y=coorLine, image=pygame.image.load("assets/Gardien.png").convert_alpha())
                elif letter == 'P':
                    self.player=MacGyver(x=coorLetter, y=coorLine, image=pygame.image.load("assets/MacGyver.png").convert_alpha())
                    self.floor.append((self.player.y,self.player.x))
                else:
                    self.floor.append((coorLine, coorLetter))

        """'item_list' is a list of dictionnaries located in 'constantes' file.
        In the following loop, for each dictionnary of 'item_list' registered,
        we will create 'Game' objects. (y,x) coordinates of each object
        will be randomly attributed from 'self.floor' list, creating 'coor_val'
        variable. Objects will be saved into 'item_object' list.

        As 'self.floor' is a list of tuples like following: (y,x), we will use
        the first number of random tuple to attribute y and the second one
        to attribute x.
        Each coordinates tuple (y,x) will be saved into 'coor_val_tuple' variable.
        If this tuple already exists in 'self.item_dict' dictionnary,
        another tuple from 'self.floor' will be randomly chosen.

        Finally, 'self.loot' object will be added to 'item_dict' dictionnary
        as key, and 'coor_val_tuple' as value.
        """
        for i in item_list:
            coor_val=random.choice(self.floor)
            loot=self.item_object.append(Item(x=coor_val[1],y=coor_val[0],name=i['name'],image=i['image']))
            for loot in self.item_object:
                coor_val_tuple=(loot.y,loot.x)
                self.item_dict[loot] = coor_val_tuple
                for value in self.item_dict:
                    if self.item_dict[value] == coor_val_tuple:
                        continue

    def lab_printing(self,background,sprite_width,sprite_height):

        """Line from 0 to 14 and column from 0 to 14 : the method compare each
        (coorLine,coorLetter) coordinates to player, guardian, walls
        and floor ones.
        According to the result, the method print the appropriate image
        """

        # for each line coordinates (= y) from 0 to 14
        for i in range(0,15):

            # for each column coordinates (= x) from 0 to 14
            for j in range(0,15):

                # (coorLine,coorLetter) tuple is compared to 'self.walls' ones
                if (i,j) in self.walls:

                    """If 'mushroom' is still registered as a name,
                    it means that the object still exists.
                    Walls will be printed as expected.
                    """          
                    for loot in self.item_object:
                        if loot.name == 'mushroom':
                            self.image="assets/wall.png"

                        else:
                            """If 'mushroom' doesn't exist as a loot anymore, it means
                            MacGyver caught it : walls image is changing.
                            """
                            self.image="assets/Groovy.png"

                        # Pygame gets saves and converts walls image
                        self.walls_img = pygame.image.load(self.image).convert_alpha()

                        # Pygame prints walls image (position corresponds to image size * coordinates)
                        background.blit(self.walls_img,(j*sprite_height,i*sprite_width))

                elif j==self.player.x and i==self.player.y:
                    background.blit(self.player.image,(j*sprite_height,i*sprite_width))

                elif j==self.guardian.x and i==self.guardian.y:
                    background.blit(self.guardian.image,(j*sprite_height,i*sprite_width))
                
                elif (i,j) in self.floor:
                    """As items coordinates are chosen from floor coordinates,
                    we have to compare floor position to items ones, in order to know
                    which image (item or floor one) has to be printed by Pygame
                    """

                    # artifact does not exist yet
                    artifact=False
                    for loot in self.item_object:
                        if j==loot.x and i==loot.y:
                                if loot.x==self.player.x and loot.y==self.player.y:
                                    continue
                                else:
                                    # artifact exists
                                    artifact=True
                                    loot_img = pygame.image.load(loot.image).convert_alpha()
                                    background.blit(loot_img,(j*sprite_height,i*sprite_width))

                    if artifact==False:
                        floor_img = pygame.image.load("assets/floor.png").convert_alpha()
                        background.blit(floor_img,(j*sprite_height,i*sprite_width))

