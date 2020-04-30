# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:28:25 2020

@author: fabie
"""
from Pion import Pion

class Joueur():
    
    
    def __init__(self, nom, couleur):
        self._nom = nom
        self._couleur = couleur
        self.nb_pion=[]
        
        for i in range(3):
            pion=Pion(self.couleur,i+1)
            self.nb_pion.append(pion)
        #les 3 pions du joueur
        self.pion1=None
        self.pion2=None
        self.pion3=None
        self.glissement_x2=False #defini si le joueur à utilisé le double glissement
        
    def get_nb_pion(self):
        return self.nb_pion
    
    def affiche_pion(self):
        return self.nb_pion.index(1)

    """protection  attribut"""
    def _get_nom(self):
        return self._nom
    
    def _get_couleur(self):
        return self._couleur
    
    nom = property(_get_nom)
    couleur = property(_get_couleur)    