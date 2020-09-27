# pygame import
from items import Item
# import random
# pygame initialization


class Guardian(Item):     # with sprite method
    def guardian(self, type):
        super().__init__()
        self.type = type

guardian = Guardian("your enemy")

print(guardian.type)
