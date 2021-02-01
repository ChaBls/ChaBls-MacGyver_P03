# !/usr/bin/env python
# -*- coding:Utf8 -*-
import os 
import sys
import pygame
from Entities.guardian import Guardian
from Entities.items import Item
from Config.constantes import ITEM_LIST
from Entities.macgyver import MacGyver
import random

# Initialize Pygame
pygame.init()


class Game:
    def __init__(self):
        # Initialize Game attributes

        # empty lists
        self.walls=[]
        self.floor=[]
        self.item_object=[]
        #empty dictionnary
        self.item_dict={}
        # walls image
        self.wall_picture="Entities/assets/wall.png"


    def lab_reading(self):
        # Open labyrinth file and save it in the variable 'file'
        file = open("Config/labyrinth.txt","r").readlines()
        
        # From 'file', get line coordinates, save it in the variable 'coorLine'
        for coorLine, line in enumerate(file):

            # From 'file', get letter coordinates, save it in the variable 'coorLetter'
            for coorLetter, letter in enumerate(line):
                """If the letter corresponds to 'M', we will add its position to 'self.walls' list

                In case the letter is 'G': we create 'guardian' object from Guardian class 
                ('guadian' file)
                In case the letter is 'P': we create 'player' object from MacGyver class
                ('macgyver' file)
                
                'coorLine' and coorLetter will be used as objects coordinates (y,x)

                If none of the above, it's corresponding to floor : we add their
                coordinates to 'self.floor' list
                """

                if letter == '\n':
                    continue
                elif letter == 'M':
                    self.walls.append((coorLine,coorLetter))
                elif letter == 'G':
                    self.guardian=Guardian(type="ennemy", x=coorLetter, y=coorLine, image=pygame.image.load("Entities/assets/Gardien.png").convert_alpha())
                elif letter == 'P':
                    self.player=MacGyver(x=coorLetter, y=coorLine, image=pygame.image.load("Entities/assets/MacGyver.png").convert_alpha())
                    self.floor.append((self.player.y,self.player.x))
                else:
                    self.floor.append((coorLine, coorLetter))

        """An empty list nammed 'items_coord' is created.

        'ITEM_LIST' is a list of 4 dictionnaries that we created in 'constantes' file.
        Each dictionnary contains 3 definitions ('name', 'image' and 'drug').

        For each dictionnary of this list and while 'success' boolean is 'False',
        the following method is randomly chosing (y,x) tuple from 'self.floor' list
        and saves it into 'coor_val' variable.

        If this tuple is matching with player coordinates or already exists
        in 'items_coord', another tuple will be randomly chosen.

        If none of the above, an 'Item' object is created, using 'coor_val' as
        coordinates (y,x).
        'coor_val' tuple is registred in 'items_coord' list
        'success' boolean is now 'True'
        """
        
        items_coord=[]
        for i in ITEM_LIST:
            success=False
            while not success:
                coor_val=random.choice(self.floor)
                if coor_val == (self.player.y,self.player.x):
                    continue
                elif coor_val in items_coord:
                    continue
                else:
                    self.item_object.append(Item(x=coor_val[1],y=coor_val[0],name=i['name'],image=i['image'],drug=i['drug']))
                    items_coord.append(coor_val)
                    success=True

    def lab_printing(self,background,sprite_width,sprite_height):

        """Line from 0 to 14 and column from 0 to 14 : the method compare each
        (coorLine,coorLetter / y,x) coordinates to player, guardian, walls
        and floor ones.
        According to the result, the method prints the appropriate image
        """

        # for each line coordinates (= y) from 0 to 14
        for i in range(0,15):

            # for each column coordinates (= x) from 0 to 14
            for j in range(0,15):

                # (coorLine,coorLetter) tuple is compared to 'self.walls' ones
                if (i,j) in self.walls:
                    if self.player.high == True:
                        self.wall_picture="Entities/assets/Groovy.png"
                    else:
                        pass

                    # Pygame gets saves and converts walls image
                    self.walls_img = pygame.image.load(self.wall_picture).convert_alpha()

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

                    floor_img = pygame.image.load("Entities/assets/floor.png").convert_alpha()
                    artifact=False
                    for loot in self.item_object:
                        if j==loot.x and i==loot.y:
                            artifact=True
                            loot_img = pygame.image.load(loot.image).convert_alpha()
                            background.blit(loot_img,(j*sprite_height,i*sprite_width))

                    if artifact==False:
                        background.blit(floor_img,(j*sprite_height,i*sprite_width))

