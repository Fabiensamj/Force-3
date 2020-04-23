# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:09:25 2020

@author: fabie
"""
import Carre_noir.py


class Plateau_jeu: # Définition de notre classe Plateau_Jeu
    
    """Classe définissant un Plateau de Jeu caractérisée par :
    -une grille 3 * 3 
    - 8 carrés_noirs disposé initialement sur cette grille({1,1,1},{1,0,1},{1,1,1})
    ces carrés noirs sont déplaçable si il y a une case vide autour de lui.
    Ils ne sont pas déplaçable en diagonale.
    - 1 pion sur chaque carré

    
    def __init__(self): # Notre méthode constructeur
        """Pour l'instant, on ne va définir qu'un seul attribut"""
        self.nom = "Dupont"