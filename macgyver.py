# !/usr/bin/env python
# -*- coding:Utf8 -*- 
# pygame import
from constantes import *
from guardian import Guardian
from items import Item
# pygame initialization


class MacGyver:     # with sprite method
    def __init__(self, name, type, image, velocity, x, y, score, over):
        self.name=name
        self.type=type
        self.image=image  # get and load self image
        self.velocity=velocity
        self.score=score
        self.over=over
        self.x=x
        self.y=y
        self.direction=direction

    def direction_update(self):
        xPosition = get_x_position
        yPosition = get_y_position
        if self.direction == 'L':   # KEYLEFT
            self.rect.x -= tile_size    # player movement do not exceed tile_size (= one square)
            self.direction = '-'
        elif self.direction == 'R':     # KEYRIGHT
            self.rect.x += tile_size
            self.direction = '-'
        elif self.direction == 'U':     # KEYUP
            self.rect.y -= tile_size
            self.direction = '-'
        elif self.direction == 'D':     # KEYDOWN
            self.rect.y += tile_size
            self.direction = '-'
          
    def score_update(self):
        pass

    def caught_item(self):
         # if player caught any item of "items_group":  -> event
            # print someting positive
            # elif player dont caught anything: -> event
                # print someting motivating
            # elif player caught all the items of "items_group":    -> event
                # print congratulations and indicate that the player still has to fight his ennemy(guardian.type)the guardian(guardian.name)

    def guardian_interaction(self):
        # if player and guardian collides with player having all the items of items_group into his inventory:
            # print congratulations, the player won
            # game quit
            # elif player and guardian collides with player not having all the items required into his inventory:
                # print "Game over, you lose"
                # game reset
