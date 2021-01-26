# !/usr/bin/env python
# -*- coding:Utf8 -*-
from Entities.items import Item


class Guardian():
    def __init__(self,x,y,type,name=None,image=None):
        Item.__init__(self,x,y,name=None,image=None,drug=None)
        self.name=name
        self.image=image
        self.rect=self.image.get_rect()
        self.type=type