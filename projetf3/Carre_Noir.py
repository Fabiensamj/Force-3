# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 14:52:01 2020

@author: fabie
"""


class Carre_Noir: # Définition de notre classe Carre_Noir
    """Classe définissant un Carré noir caractérisée par :
    - sa position x dans la grille 3*3 du plateau du jeu
    - sa position y dans la grille 3*3 du plateau du jeu
    - 
    - 
"""
    
    def __init__(self,x,y): # Notre méthode constructeur
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self.x=x
        self.y=y
        self.pion = None

    def __str__(self):
        return "N"
    
    def Deplacer_Carre(self,x,y):
        self.x=x
        self.y=y