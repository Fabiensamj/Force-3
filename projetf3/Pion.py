# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:50:13 2020

@author: jeome
"""

## réfléchir identifiant

class Pion():
    
    def __init__(self, color):
        #self._id = identite
        self._x = None
        self._y = None
        self._couleur = color
        
    def _get_x(self):
        return self._x
    def _set_x(self, new_x):
        self.x = new_x
        
    def _get_y(self):
        return self._y
    def _set_y(self, new_y):
        self.x = new_y
        
    def _get_couleur(self):
        return self._couleur
    
    """def _get_id(self):
        return self._id"""
    
    #identifiant = property(_get_id())
    x = property(_get_x(),_set_x())
    y = property(_get_y(),_set_y())
    couleur = property(_get_couleur())
    
    def deplacer_pion(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
    