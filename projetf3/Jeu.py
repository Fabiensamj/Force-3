# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 17:13:55 2020

@author: fabie
"""

from Carre_Noir import *
from Plateau_Jeu import *
from Pion import *
from Joueur import *


def Init_partie():
    nom1 = input("Joueur 1 entrez votre nom: ")
    couleur1 = input("Joueur 1 choisissez votre couleur (rouge ou bleu): ")
    nom2 = input("Joueur 2 entrez votre nom: ")
    couleur2 = input("Joueur 2 choisissez votre couleur (rouge ou bleu): ")
    
    j1 = Joueur(nom1,couleur1)
    j2 = Joueur(nom2,couleur2)
    
    
    
    plateau = Plateau_jeu()
    plateau.affichePlateau()
    
        
        
    

       
    
       
       
       
       
       
"""main test"""

Init_partie()
        