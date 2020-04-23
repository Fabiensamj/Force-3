# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:09:25 2020

@author: fabie
"""

from Carre_Noir import *

import numpy as np







    


class Plateau_jeu: # Définition de notre classe Plateau_Jeu
    
    """Classe définissant un Plateau de Jeu caractérisée par :
    -une grille 3 * 3 
    - 8 carrés_noirs disposé initialement sur cette grille({1,1,1},{1,0,1},{1,1,1})
    ces carrés noirs sont déplaçable si il y a une case vide autour de lui.
    Ils ne sont pas déplaçable en diagonale.
    - 1 pion sur chaque carré
    """
    
    def __init__(self): # Notre méthode constructeur
       """Pour l'instant, on ne va définir qu'un seul attribut"""
        
       self.tab = np.empty([3, 3], dtype=Carre_Noir)           
                

       for i in range(3):
           for j in range(3):
               if(i == 1 and j == 1):
                   self.tab[i,j] = None
               else:
                   a=Carre_Noir(i,j)
                   self.tab[i][j] = a
                   #print(self.tab[i,j])
                


    def affichePlateau(self): #afficher le plateau du jeu
        
        show_tab= np.copy(self.tab)
        for i in range(3):
            for j in range(3):
                if(show_tab[i,j] == None):
                    show_tab[i,j]=' '
                else: 
                    show_tab[i,j]= 'N'
            
        
        print(self.tab)
        print(show_tab)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        