# !/usr/bin/env python
# -*- coding:Utf8 -*-
import pygame
from guardian import Guardian
from items import Item
from constantes import item_list
from macgyver import MacGyver
import random
pygame.init()


class Game:
    def __init__(self):
        self.walls=[]
        self.floor=[]
        self.item_object=[]
        self.item_dict={}

    def lab_reading(self):
        file = open("labyrinth.txt","r").readlines()
        # Open labyrinth file and save it in the variable 'file'
        
        for coorLine, line in enumerate(file):
        # Get line coordinates (from file), save it in coorLine

            for coorLetter, letter in enumerate(line):
            # Get letter coordinates (from line), save it in coorLetter

                """If the letter corresponds to 'M', we will add its position to walls list
                If the letter corresponds to 'P' or 'G', we'll create player
                or guardian objects, with their own position.
                If the letter is 'M', we add it in list of walls 'self.walls'.
                What if the letter is 'G': we create 'guardian' object from Guardian class.
                What if the letter is 'P': we create 'player' object from MacGyver class.
                If none of the above, it will be empty spaces: we add their
                coordinates to 'self.floor' list.
                """
                if letter == "\n":
                    continue
                elif letter == 'M':
                    self.walls.append((coorLine,coorLetter))
                elif letter == 'G':
                    self.guardian=Guardian(type="ennemy", x=coorLetter, y=coorLine, image="assets/Gardien.png")
                elif letter == 'P':
                    self.player=MacGyver(x=coorLetter, y=coorLine, image="assets/MacGyver.png")
                    self.floor.append((self.player.y,self.player.x))
                else:
                    self.floor.append((coorLine, coorLetter))

        """In the following loop, for each item of 'item_list list, we will attribute
        random coordinates from 'self.floor' list, as 'coor_val'.
        If these coordinates already exist in 'self.item_dict' dictionnary,
        another tuple from 'self.floor' will be randomly chosen.
        If 'coor_val' doesn't exist in the dictionnary, Item() instance will be created
        as 'self.loot', then added to 'item_object' list.
        Finally, 'self.loot' object will be added to the dictionnary as key,
        with 'coor_val' as value.
        """
        for i in item_list:
            coor_val=random.choice(self.floor)
            loot=self.item_object.append(Item(x=coor_val[1],y=coor_val[0],name=i['name'],image=i['image']))
            for loot in self.item_object:
                coor_val_tuple=(loot.y,loot.x)
                self.item_dict[loot] = coor_val_tuple
                if coor_val_tuple in self.item_dict:
                    continue

    def lab_printing(self):

        """Line from 0 to 14 and column from 0 to 14 : the method compare each
        character position to player, guardian, walls and floor coordinates.
        According to the result, the method print the appropriate letter
        ('M' for walls, 'P' for player or 'G' for guardian and empty space for floors).
        """

        for i in range(0,15):
            for j in range(0,15):
                if (i,j) in self.walls:
                    pygame.image.load("assets/prisma.jpg").convert_alpha()
                elif j==self.player.x and i==self.player.y:
                    pygame.image.load(self.player.image).convert_alpha()
                elif j==self.guardian.x and i==self.guardian.y:
                    pygame.image.load(self.guardian.image).convert_alpha()
                elif (i,j) in self.floor:
                    artifact=False
                    for loot in self.item_object:
                        if j==loot.x and i==loot.y:
                            artifact=True
                            pygame.image.load(loot.image).convert_alpha()
                    if artifact==False:
                        pygame.image.load("assets/floor.jpg").convert_alpha()
