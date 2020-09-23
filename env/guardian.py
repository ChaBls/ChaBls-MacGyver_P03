# import the proper modules
import random
from items import Item
# initialization


class Guardian(Item):     # with sprite method
    def __init__(self):
        self.name = "Guardian"
        self.type = "ennemy"
        self.image = image  # get and load self image
        self.rect = rect    # get image rect
        self.rect.x = rect.x  # random y position
        self.rect.y = rect.y  # random y position

guardian = Guardian()
