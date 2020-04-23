# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:28:25 2020

@author: fabie
"""
from Pion import *

class Joueur():
    
    
    def __init__(self, nom, couleur):
        self.nom = nom
        self.couleur = couleur
        self.nb_pion=[]
        
        for i in range(3):
            pion=Pion(self.couleur)
            self.nb_pion.append(pion)


    def get_nb_pion(self):
        return self.nb_pion
    
    def affiche_pion(self):
        return self.nb_pion.index(1)


