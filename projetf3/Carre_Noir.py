# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:52:01 2020

@author: fabie
"""
#from Pion import Pion

class Carre_Noir: # Définition de notre classe Carre_Noir
    """Classe définissant un Carré noir caractérisée par :
    - sa position x dans la grille 3*3 du plateau du jeu
    - sa position y dans la grille 3*3 du plateau du jeu
    - 
    - 
"""
    
    def __init__(self,x,y): # Notre méthode constructeur
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self._x=x
        self._y=y
        self._pion = None

    def __str__(self):
        return "N" 
    
    def Deplacer_Carre(self,x,y):
        self._x=x
        self._y=y
        
        """protection attribut"""
        
     
    def _get_x(self):
        return self._x
    def _set_x(self, new_x):
        self._x = new_x
        
    def _get_y(self):
        return self._y
    def _set_y(self, new_y):
        self._y = new_y
    
    def _get_pion(self):
        return self._pion
    def _set_pion(self, pion):
        self._pion=pion
     
    x = property(_get_x,_set_x)
    y = property(_get_y,_set_y)
    pion = property(_get_pion,_set_pion)
    
"""test pion et carre_noir"""
"""c=Carre_Noir(1,2)
print(c.x,c.y)
c.x=2
c.y=1
c.pion=Pion("rouge")

print(c.x,c.y,c.pion.couleur)"""