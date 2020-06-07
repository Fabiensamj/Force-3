# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:09:25 2020

@author: fabie
"""



import numpy as np

class Pion():
    """on définit un Pion possédant une couleur (rouge ou bleu) et des coordonnées
    x et y désignant son emplacement sur le plateau de jeu"""
    
    def __init__(self, color, identite):
        self._id = identite
        self._x = None
        self._y = None
        self._couleur = color
        
        
    def deplacer_pion(self, new_x, new_y):
        self._x = new_x
        self._y = new_y
        
        """protection attribut"""
    def _get_x(self):
        return self._x
    def _set_x(self, new_x):
        self._x = new_x
        
    def _get_y(self):
        return self._y
    def _set_y(self, new_y):
        self._y = new_y
        
    def _get_couleur(self):
        return self._couleur
    
    def _get_id(self):
        return self._id
    
    i_d = property(_get_id)
    x = property(_get_x,_set_x)
    y = property(_get_y,_set_y)
    couleur = property(_get_couleur)

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
       self.i_none = 1
       self.j_none = 1

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
                    show_tab[i,j]='Vide'
                elif show_tab[i,j].pion != None:
                    I_d = str(show_tab[i,j].pion.i_d)
                    show_tab[i,j]='N - pion'+I_d+' '+ show_tab[i,j].pion.couleur
                else: 
                    show_tab[i,j]= 'N'
                    
        #print(self.tab)
        print(show_tab)
        print("\n")

    def __getitem__(self,tup):
        i,j = tup
        return self.tab[i][j]
    
    def __setitem__(self,tup,valeur):
        i,j = tup
        self.tab[i,j]=valeur
        
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
        
"""test plateau"""
"""
P=Plateau_jeu()
P.affichePlateau()
print(P[0,0],P[1,1])
P[0,0]=None
print(P[0,0],P[1,1])       
a=P[1,2]
""" 
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        