# !/usr/bin/env python
# -*- coding:Utf8 -*-
from Entities.items import Item


class Guardian():
    """This class is related to Item one.
    Most of guardian attributes are 'None' by default
    and are setted in 'lab_reading' ('game' file), when
    Guardian object is created.
    """
    
    def __init__(self,x,y,type,name=None,image=None):
        Item.__init__(self,x,y,name=None,image=None,drug=None)
        self.name=name
        self.image=image
        self.rect=self.image.get_rect()
        self.type=type
