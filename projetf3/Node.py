# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:08:45 2020

@author: fabie et jeoffrey
"""
import copy
from sys import maxsize
from Pion import Pion
from Carre_Noir import Carre_Noir

from Jouer import Jouer
from Jouer import victoire
from Plateau_Jeu import Plateau_jeu
from Joueur import Joueur

##======================================================================
##=======================Aretes de l'arbre====================================
##====================================================================== 
class Arete_Action():
    
    def __init__(self, num_action, x=None, y=None,num_pion=None):
        self._num_action = num_action
        self._x = x
        self._y = y
        self._num_pion = num_pion
    def _get_num_action(self):
        return self._num_action
    
    def _get_x(self):
        return self._x
    
    def _get_y(self):
        return self._y
    
    def _get_num_pion(self):
        return self._num_pion
    
    num_action = property(_get_num_action)
    x = property(_get_x)
    y = property(_get_y)
    num_pion = property(_get_num_pion)
##======================================================================
##=======================Création de l'arbre============================
##====================================================================== 

class Node():
    def __init__(self,profondeur,joueur,autre_joueur,plateau,action_joue = None, valeur = 0):
        self.profondeur=profondeur
        self.joueur=joueur
        self.autre_joueur=autre_joueur
        self.action=action_joue
        self.valeur=valeur
        self.enfants= []
        self.plateau=plateau
        self.jeu = Jouer(copy.deepcopy(self.plateau),copy.deepcopy(self.joueur),copy.deepcopy(self.autre_joueur))
        self.creer_enfants()
        
    def actions_possibles(self):
        
        res_actions = []
        if victoire(self.joueur,self.plateau) != True:
            
            cout_double = self.autre_joueur.glissement_x2
       
            if (self.joueur.nb_pion[0] != None):
                res_actions = [1,2]
            
            elif (self.joueur.nb_pion[0] == None and self.joueur.nb_pion[2] != None ):
                res_actions = [1,2,3]
            
            else :
                res_actions = [2,3]
            
            if ((cout_double==False) and 
                ((self.plateau.i_none == 0 and self.plateau.j_none == 1) or 
                  (self.plateau.i_none == 1 and self.plateau.j_none == 0) or 
                  (self.plateau.i_none == 2 and self.plateau.j_none == 1) or 
                  (self.plateau.i_none == 1 and self.plateau.j_none == 2))):
                res_actions.append(4)
                self.joueur.glissement_x2 = True
            
            if self.autre_joueur.glissement_x2 == True:
                self.autre_joueur.glissement_x2 == False
            
            
        return res_actions
        
    def creer_enfants(self):
        for i in range(3):
            for j in range(3):
                if (self.plateau[i,j] != None and self.plateau[i,j].pion != None):
                    idt = self.plateau[i,j].pion.i_d
                    
                    couleur = self.plateau[i,j].pion.couleur
                    if self.joueur.couleur == couleur:
                        if idt == 1:
                            self.joueur.pion1.x,self.joueur.pion1.y = self.plateau[i,j].x,self.plateau[i,j].y
                        if idt == 2:
                            self.joueur.pion2.x,self.joueur.pion2.y = self.plateau[i,j].x,self.plateau[i,j].y
                        if idt == 3:
                            self.joueur.pion3.x,self.joueur.pion3.y = self.plateau[i,j].x,self.plateau[i,j].y
                    
                    else:
                        if idt == 1:
                            self.autre_joueur.pion1.x,self.autre_joueur.pion1.y = self.plateau[i,j].x,self.plateau[i,j].y
                        if idt == 2:
                            self.autre_joueur.pion2.x,self.autre_joueur.pion2.y = self.plateau[i,j].x,self.plateau[i,j].y
                        if idt == 3:
                            self.autre_joueur.pion3.x,self.autre_joueur.pion3.y = self.plateau[i,j].x,self.plateau[i,j].y
        
        coups_permis = self.actions_possibles()
        
        if self.profondeur > 0 and coups_permis != []:
            
            for i in range(len(coups_permis)):
                coup = coups_permis[i]
                
                
                
                
                if coup == 1:
                    
                    for x in range(3):
                        for y in range(3):
                            self.jeu.plateau = copy.deepcopy(self.plateau)
                            self.jeu.j1 = copy.deepcopy(self.joueur)
                            self.jeu.j2 = copy.deepcopy(self.autre_joueur)
                            
                            
                            if ((x,y) != (self.jeu.plateau.i_none,self.jeu.plateau.j_none) and 
                                self.jeu.plateau[x,y].pion == None):
                                
                                self.jeu.poser_pion(self.jeu.j1,self.jeu.plateau[x,y])
                                action = Arete_Action(1,x,y)
                                self.enfants.append(Node(self.profondeur-1,self.jeu.j2,
                                                         self.jeu.j1,self.jeu.plateau,action))
                                
                                
                if coup == 2:
                  
                    for x in range(3):
                        for y in range(3):
                            self.jeu.plateau = copy.deepcopy(self.plateau)
                            self.jeu.j1 = copy.deepcopy(self.joueur)
                            self.jeu.j2 = copy.deepcopy(self.autre_joueur)
                            
                            if ((x,y) != (self.jeu.plateau.i_none,self.jeu.plateau.j_none) and 
                                (self.jeu.plateau.i_none == x and self.jeu.plateau.j_none == y-1) or
                                (self.jeu.plateau.i_none == x and self.jeu.plateau.j_none == y+1) or
                                (self.jeu.plateau.i_none == x-1 and self.jeu.plateau.j_none == y) or
                                (self.jeu.plateau.i_none == x+1 and self.jeu.plateau.j_none == y)):
                         
                                self.jeu.deplacement_glissement(self.jeu.plateau[x,y])
                                action = Arete_Action(2,x,y)
                                self.enfants.append(Node(self.profondeur-1,self.jeu.j2,
                                                         self.jeu.j1,self.jeu.plateau,action))
                              
                if coup == 3:
                    
                    if self.joueur.pion1 != None:
                        for x in range(3):
                            for y in range(3):
                                self.jeu.plateau = copy.deepcopy(self.plateau)
                                self.jeu.j1 = copy.deepcopy(self.joueur)
                                self.jeu.j2 = copy.deepcopy(self.autre_joueur)
                                
                                if ((x,y) != (self.jeu.plateau.i_none,self.jeu.plateau.j_none) and
                                    self.jeu.plateau[x,y].pion == None):
                                    
                                    self.jeu.deplacer_pion(self.jeu.j1,self.jeu.j1.pion1,self.jeu.plateau[x,y])
                                    action = Arete_Action(3,x,y,1)
                                    self.enfants.append(Node(self.profondeur-1,self.jeu.j2,
                                                         self.jeu.j1,self.jeu.plateau,action))
                                    
                    if self.joueur.pion2 != None:
                        for x in range(3):
                            for y in range(3):
                                self.jeu.plateau = copy.deepcopy(self.plateau)
                                self.jeu.j1 = copy.deepcopy(self.joueur)
                                self.jeu.j2 = copy.deepcopy(self.autre_joueur)
                                if ((x,y) != (self.jeu.plateau.i_none,self.jeu.plateau.j_none) and
                                    self.jeu.plateau[x,y].pion == None):
                                     
                                    self.jeu.deplacer_pion(self.jeu.j1,self.jeu.j1.pion2,self.jeu.plateau[x,y])
                                    action = Arete_Action(3,x,y,2)
                                    self.enfants.append(Node(self.profondeur-1,self.jeu.j2,
                                                         self.jeu.j1,self.jeu.plateau,action))
                                    
                    if self.joueur.pion3 != None:
                        for x in range(3):
                            for y in range(3):
                                self.jeu.plateau = copy.deepcopy(self.plateau)
                                self.jeu.j1 = copy.deepcopy(self.joueur)
                                self.jeu.j2 = copy.deepcopy(self.autre_joueur)
                             
                                if ((x,y) != (self.jeu.plateau.i_none,self.jeu.plateau.j_none) and
                                    self.jeu.plateau[x,y].pion == None):
                                    
                                    self.jeu.deplacer_pion(self.jeu.j1,self.jeu.j1.pion3,self.jeu.plateau[x,y])
                                    action = Arete_Action(3,x,y,3)
                                    self.enfants.append(Node(self.profondeur-1,self.jeu.j2,
                                                         self.jeu.j1,self.jeu.plateau,action))
                                    
                
                                    
                if coup == 4:
                    self.jeu.plateau = copy.deepcopy(self.plateau)
                    self.jeu.j1 = copy.deepcopy(self.joueur)
                    self.jeu.j2 = copy.deepcopy(self.autre_joueur)
                    
                    self.jeu.double_glissement()
                    action = Arete_Action(4)
                    self.enfants.append(Node(self.profondeur-1,self.jeu.j2,
                                        self.jeu.j1,self.jeu.plateau,action))
                    
       
                    
    def affiche(self):
        print("pere")
        self.plateau.affichePlateau()
        print("enfants")
        for i in range(len(self.enfants)):
            self.enfants[i].plateau.affichePlateau()
                            

###test###
node = Node(4,Joueur("jean","r"),Joueur("pierre","b"),Plateau_jeu())                  
node.affiche()
node.enfants[0].affiche()
node.enfants[0].enfants[0].affiche()
node.enfants[0].enfants[0].enfants[0].affiche()
#node.enfants[0].enfants[0].enfants[8].enfants[16].affiche()
"""        
#=======================================
    def bestMove() {
    # AI to make its turn
    bestScore = -maxsize
    for i in range(3):
        for j in range(3):
            if(plateau[i,j].pion == None):
                plateau[i,j].pion = ia
                score = minMax(plateau,0,false)
                plateau[i,j].pion = None
                if(score>bestScore):
                    bestscore = score
                    action = [i,j]
    plateau[action.i][action.j].pion = ia
    chgt_joueur = human
    
                
def minMax(plateau,profondeur,estMax):
    resultat = victoire(Joueur)
    if (resultat):
        return scores[resultat]
    
    
    if (estMax):
        bestScore = -maxsize
        for i in range(3):
            for j in range(3): 
                #check si ya un emplacement libre
                if(plateau[i,j] == None):
                    plateau[i,j]=ia
                    score=minMax(plateau, profondeur+1, False)
                    plateau[i,j]=None
                    bestscore=max(score,bestscore)
        return bestscore
    else:
        bestscore=maxsize
        for i in range(3):
            for j in range(3): 
                #check si ya un emplacement libre
                if(plateau[i,j] == None):
                    plateau[i,j]=humain
                    score=minMax(plateau, profondeur+1, True)
                    plateau[i,j]=None
                    bestscore=min(score,bestscore)
        return bestscore
        
    
#=======================================
        
    def create_Children(self):
        if self.i_profondeur >=0:
            
 """           
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        