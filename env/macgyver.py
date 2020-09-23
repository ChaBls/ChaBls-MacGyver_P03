# import the proper modules
from constantes import *
from guardian import *
from items import Item
# module initialization


class macGyver:     # with sprite method
    def __init__(self, name, type, image, velocity, x, y, score, over):
        self.name = "Mac Gyver"
        self.type = "heroe"
        self.image =    # get and load self image
        self.velocity: int
        self.rect.x = int
        self.rect.y = int
        self.direction = str
        self.score = str
        self.over = bool 

    def directions_update(self):
        xPosition = get_x_position
        yPosition = get_y_position
        # if self right direction(x axis):
            # go to the right
           # get_x_position based on walls_tile_size
        # elif self left direction(x axis):
            # go to the left
            # get_x_position based on walls_tile_size
        # elif self up direction(y axis):
            # go up
            # get_y_position based on walls_tile_size
        # elif self down direction(y axis):
            # go down
            # get_y_position based on walls_tile_size

    def score_update(self):
        pass

    def caught_item(self):
         # if player caught any item of "items_group":
            # print someting positive
            # elif player dont caught anything:
                # print someting motivating
            # elif player caught all the items of "items_group":
                # print congratulations and indicate that the player still has to fight his ennemy(guardian.type)the guardian(guardian.name)

    def Collision(self):
        # configure sprite collide between player and items_group
        # configure sprite collide between player and env_group
        # configure sprite collide between player and guardian

    def guardianInteraction(self):
        # if player and guardian collides with player having all the items of items_group into his inventory:
            # print congratulations, the player won
            # game quit
            # elif player and guardian collides with player not having all the items required into his inventory:
                # print "Game over, you lose"
                # game reset

player = macGyver()
