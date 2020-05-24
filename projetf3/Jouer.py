# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:53:08 2020

@author: jeome
"""
from Pion import Pion
from Carre_Noir import Carre_Noir
from Joueur import Joueur
from Plateau_Jeu import Plateau_jeu
from Node import *
import copy
import numpy as np
import math
import random

class Jouer:
    """ cette classe va définir toutes les actions que les joueurs peuvent faire 
    durant leur partie et qui va modifier le plateau de jeu"""
    
    def __init__(self,plateau_de_jeu,joueur1,joueur2):
        self.plateau = plateau_de_jeu
        self.j1=joueur1
        self.j2=joueur2
        
    def poser_pion(self,joueur,carre):
        """ on regarde si tous les pions du joueur sont sur le plateau ou non """
        i=0
        while joueur.nb_pion[i]==None and i<len(joueur.nb_pion): 
            i+=1
        
        """ on déplace le piont sur le carre noir voulu"""
        joueur.nb_pion[i].x = carre.x 
        joueur.nb_pion[i].y = carre.y
        
        """ on détermine quelle pion a été jouer par le joueur et on l'affecte au carre noir """
        if i==0:
            joueur.pion1=joueur.nb_pion[i]
            carre.pion = joueur.pion1
        elif i==1:
            joueur.pion2=joueur.nb_pion[i]
            carre.pion = joueur.pion2
        else:
            joueur.pion3=joueur.nb_pion[i]
            carre.pion = joueur.pion3
        
        """ on retire le pion poser de la liste du joueur car le pion est désormais sur le plateau de jeu"""
        joueur.nb_pion[i]=None 
        
    def deplacer_pion(self,joueur,pion,carre):
        """ on déplace le pion souhaité (pion1,pion2 ou pion3) dans la case du carré voulu et on ajoute ce pion 
        dans l'espace du carré """
        if pion==joueur.pion1:
            i,j = joueur.pion1.x, joueur.pion1.y
            joueur.pion1.deplacer_pion(carre.x,carre.y)
            carre.pion = joueur.pion1
            self.plateau[i,j].pion = None
        
        elif pion==joueur.pion2:
            i,j = joueur.pion2.x, joueur.pion2.y
            joueur.pion2.deplacer_pion(carre.x,carre.y)
            carre.pion = joueur.pion2
            self.plateau[i,j].pion = None
        
        else:
            i,j = joueur.pion3.x, joueur.pion3.y
            
            joueur.pion3.deplacer_pion(carre.x,carre.y)
            carre.pion = joueur.pion3
            
            self.plateau[i,j].pion = None
     
    def deplacement_glissement(self,carre):
        i=carre.x #on garde les valeurs des coordonnées du carré que l'on souhaite déplacer
        j=carre.y
        carre.x=self.plateau.i_none #les nouvelles coordonnées du carre sont celle de l'ancien espace vide
        carre.y=self.plateau.j_none
        if carre.pion != None: #si le carre possede un pion on change les coordonées du pion également
            carre.pion.x = carre.x
            carre.pion.y = carre.y
            
        self.plateau[self.plateau.i_none,self.plateau.j_none]=carre #l'ancien espace vide contient désormais le carre noir
        self.plateau[i,j]=None #l'ancienne position du carre devient l'espace vide
        self.plateau.i_none = i
        self.plateau.j_none = j #on réattribut les coordonnées de l'espace vide dans la classe plateau
        
    def double_glissement(self):
        #""" cas où l'espace vide est en haut en (0,1)"""
        if (self.plateau.i_none,self.plateau.j_none) == (0,1):
            
            #on change les coordonnées du 1er carre qui va être déplacé et du pion s'il y en a
            self.plateau[1,1].x,self.plateau[1,1].y = 0,1 
            if self.plateau[1,1].pion != None:
                self.plateau[1,1].pion.x,self.plateau[1,1].pion.y = 0,1
            #on change les coordonnées du 2e carre qui va être déplacé et du pion s'il y en a
            self.plateau[2,1].x,self.plateau[2,1].y = 1,1
            if self.plateau[2,1].pion != None:
                self.plateau[2,1].pion.x,self.plateau[2,1].pion.y = 1,1
            #on déplace les carrées sur le plateau et on y affecte le nouvel espace vide 
            self.plateau[0,1] = self.plateau[1,1]
            self.plateau[1,1] = self.plateau[2,1]
            self.plateau[2,1] = None
            self.plateau.i_none,self.plateau.j_none = 2,1
            
        #"""on fait de même pour les 3 autres cas"""
        #""" cas où l'espace vide est en haut en (2,1)"""
        elif (self.plateau.i_none,self.plateau.j_none) == (2,1):
            #on change les coordonnées du 1er carre qui va être déplacé et du pion s'il y en a
            self.plateau[1,1].x,self.plateau[1,1].y = 2,1 
            if self.plateau[1,1].pion != None:
                self.plateau[1,1].pion.x,self.plateau[1,1].pion.y = 2,1
            #on change les coordonnées du 2e carre qui va être déplacé et du pion s'il y en a
            self.plateau[0,1].x,self.plateau[0,1].y = 1,1
            if self.plateau[0,1].pion != None:
                self.plateau[0,1].pion.x,self.plateau[0,1].pion.y = 1,1
            #on déplace les carrées sur le plateau et on y affecte le nouvel espace vide 
            self.plateau[2,1] = self.plateau[1,1]
            self.plateau[1,1] = self.plateau[0,1]
            self.plateau[0,1] = None
            self.plateau.i_none,self.plateau.j_none = 0,1
        
        #""" cas où l'espace vide est en haut en (1,2)"""
        elif (self.plateau.i_none,self.plateau.j_none) == (1,2):
            #on change les coordonnées du 1er carre qui va être déplacé et du pion s'il y en a
            self.plateau[1,1].x,self.plateau[1,1].y = 1,2 
            if self.plateau[1,1].pion != None:
                self.plateau[1,1].pion.x,self.plateau[1,1].pion.y = 1,2
            #on change les coordonnées du 2e carre qui va être déplacé et du pion s'il y en a
            self.plateau[1,0].x,self.plateau[1,0].y = 1,1
            if self.plateau[1,0].pion != None:
                self.plateau[1,0].pion.x,self.plateau[1,0].pion.y = 1,1
            #on déplace les carrées sur le plateau et on y affecte le nouvel espace vide 
            self.plateau[1,2] = self.plateau[1,1]
            self.plateau[1,1] = self.plateau[1,0]
            self.plateau[1,0] = None
            self.plateau.i_none,self.plateau.j_none = 1,0
            
        #""" cas où l'espace vide est en haut en (1,0)"""
        elif (self.plateau.i_none,self.plateau.j_none) == (1,0):
            #on change les coordonnées du 1er carre qui va être déplacé et du pion s'il y en a
            self.plateau[1,1].x,self.plateau[1,1].y = 1,0 
            if self.plateau[1,1].pion != None:
                self.plateau[1,1].pion.x,self.plateau[1,1].pion.y = 1,0
            #on change les coordonnées du 2e carre qui va être déplacé et du pion s'il y en a
            self.plateau[1,2].x,self.plateau[1,2].y = 1,1
            if self.plateau[1,2].pion != None:
                self.plateau[1,2].pion.x,self.plateau[1,2].pion.y = 1,1
            #on déplace les carrées sur le plateau et on y affecte le nouvel espace vide 
            self.plateau[1,0] = self.plateau[1,1]
            self.plateau[1,1] = self.plateau[1,2]
            self.plateau[1,2] = None
            self.plateau.i_none,self.plateau.j_none = 1,2


##======================================================================#
##======================Fonctions Actions personnages===================#
##======================================================================# 


    def choix_action_ia(self,joueur):
        
        if joueur == self.j1:
            
            autre_joueur = self.j2
        else:
            autre_joueur = self.j1
        
        le_joueur = copy.deepcopy(joueur)
        lautre_joueur = copy.deepcopy(autre_joueur)
        noeud = Node(3,le_joueur,lautre_joueur,self.plateau)
        
        v = MinMaxPL(noeud, noeud.profondeur,joueur,autre_joueur)
        print(v)
        print(joueur.couleur)
        meilleure_action = []
        for i in range(len(noeud.enfants)):
            if noeud.enfants[i].valeur == v:
                meilleure_action.append(noeud.enfants[i])
                
        if len(meilleure_action) > 1:
            rand_enfant = random.choice(meilleure_action)
        
        else:
            print(meilleure_action)
            rand_enfant = meilleure_action[0]
            
        if rand_enfant.action.num_action == 1:
            self.poser_pion(joueur, self.plateau[rand_enfant.action.x,rand_enfant.action.y])
        if rand_enfant.action.num_action == 2:
            self.deplacement_glissement(self.plateau[rand_enfant.action.x,rand_enfant.action.y])
        if rand_enfant.action.num_action == 3:
            if rand_enfant.action.num_pion == 1:
                self.deplacer_pion(joueur, joueur.pion1, self.plateau[rand_enfant.action.x,rand_enfant.action.y])
            if rand_enfant.action.num_pion == 2:
                self.deplacer_pion(joueur, joueur.pion2, self.plateau[rand_enfant.action.x,rand_enfant.action.y])
            if rand_enfant.action.num_pion == 3:
                self.deplacer_pion(joueur, joueur.pion3, self.plateau[rand_enfant.action.x,rand_enfant.action.y])
        if rand_enfant.action.num_action == 4:
            self.double_glissement()
            joueur.glissement_x2=True
        if autre_joueur.glissement_x2==True:
                autre_joueur.glissement_x2 = False
       

    def choix_action_joueur(self,joueur):
        print(joueur.nom,"à vous de jouer")
        #on regarde si le joueur qui à jouer juste avant à effectuer le double glissement ou non
        if joueur == self.j1:
            cout_double = self.j2.glissement_x2
        else:
            cout_double = self.j1.glissement_x2
       
        choix1 = False
        choix2 = False
        choix3 = False
        choix4 = False
        
        if (joueur.nb_pion[0] != None):
            print("Choix action : ")
            print("1 : poser un pion ")
            print("2 : deplacer un carre noir")
            choix1 = True
            choix2 = True
            
            if ((cout_double==False) and 
            ((self.plateau.i_none == 0 and self.plateau.j_none == 1) or 
            (self.plateau.i_none == 1 and self.plateau.j_none == 0) or 
            (self.plateau.i_none == 2 and self.plateau.j_none == 1) or 
            (self.plateau.i_none == 1 and self.plateau.j_none == 2))):
                print("4 : deplacer 2 carres noirs")
                choix4 = True
                
        
        elif (joueur.nb_pion[0] == None and joueur.nb_pion[2] != None ):
            print("Choix action : ")
            print("1 : poser un pion ")
            print("2 : deplacer un carre noir")
            print("3 : deplacer un pion du plateau")
            choix1 = True
            choix2 = True
            choix3 = True
            
            if ((cout_double==False) and 
            ((self.plateau.i_none == 0 and self.plateau.j_none == 1) or 
            (self.plateau.i_none == 1 and self.plateau.j_none == 0) or 
            (self.plateau.i_none == 2 and self.plateau.j_none == 1) or 
            (self.plateau.i_none == 1 and self.plateau.j_none == 2))):
                print("4 : deplacer 2 carres noirs")
                choix4 = True
        
        else :
            print("Choix action : ")
            print("2 : deplacer un carre noir")
            print("3 : deplacer un pion du plateau")
            choix2 = True
            choix3 = True
            
            if ((cout_double==False) and 
            ((self.plateau.i_none == 0 and self.plateau.j_none == 1) or 
            (self.plateau.i_none == 1 and self.plateau.j_none == 0) or 
            (self.plateau.i_none == 2 and self.plateau.j_none == 1) or 
            (self.plateau.i_none == 1 and self.plateau.j_none == 2))):
                print("4 : deplacer 2 carres noirs")
                choix4 = True
            
        choix = int(input("veuillez choisir une action en tapant le chiffre souhaité : "))
        if choix == 1 and choix1 == True:
            print("veuillez choisir une case (x,y)")
            x = int(input("x : "))
            while x>2 or x<0 :
                print("valeur non valide: x = {0, 1, 2}")
                x = int(input("x : "))
            y = int(input("y : "))
            while y>2 or y<0:
                print("valeur non valide: y = {0, 1, 2}")
                y = int(input("y : "))
            if (x==self.plateau.i_none and y==self.plateau.j_none):
                print("La case est vide, vous ne pouvez pas poser un pion ici")
                self.choix_action_joueur(joueur)
            elif self.plateau[x,y].pion != None:
                print("Cette case contient déjà un pion")
                self.choix_action_joueur(joueur)
            else:
                self.poser_pion(joueur,self.plateau[x,y])
                    
        elif choix == 2 and choix2==True:
            print("veuillez choisir la case a deplacer (x,y)")
            x = int(input("x : "))
            while x>2 or x<0:
                print("valeur non valide: x = {0, 1, 2}")
                x = int(input("x : "))
            y = int(input("y : "))
            while y>2 or y<0:
                print("valeur non valide: y = {0, 1, 2}")
                y = int(input("y : "))
            if (x==self.plateau.i_none and y==self.plateau.j_none):
                print("La case est vide, vous ne pouvez pas la deplacer")
                self.choix_action_joueur(joueur)
            elif ((self.plateau.i_none == x and self.plateau.j_none == y-1) or
            (self.plateau.i_none == x and self.plateau.j_none == y+1) or
            (self.plateau.i_none == x-1 and self.plateau.j_none == y) or
            (self.plateau.i_none == x+1 and self.plateau.j_none == y)):
                self.deplacement_glissement(self.plateau[x,y])
            else:
                print("Cette case ne peut être déplace")
                self.choix_action_joueur(joueur)
                
        elif choix == 3 and choix3 == True:
            print("veuillez choisir le pion à déplacer (1, 2 ou 3")
            pion = int(input("je choisi le pion : "))
            if pion == 1:
                if joueur.pion1 == None:
                    print("ce pion n est pas sur le plateau")
                    self.choix_action_joueur(joueur)
                else:
                    print("choisir la case ou deplacer le pion")
                    x = int(input("x : "))
                    while x>2 or x<0:
                        print("valeur non valide: x = {0, 1, 2}")
                        x = int(input("x : "))
                    y = int(input("y : "))
                    while y>2 or y<0:
                        print("valeur non valide: y = {0, 1, 2}")
                        y = int(input("y : "))
                    if (x==self.plateau.i_none and y==self.plateau.j_none):
                        print("La case est vide, vous ne pouvez pas le deplacer ici")
                        self.choix_action_joueur(joueur)
                    if (self.plateau[x,y].pion != None):
                        print("La case est déjà occupée!")
                        self.choix_action_joueur(joueur)
                    else:
                        self.deplacer_pion(joueur,joueur.pion1,self.plateau[x,y])
                        
            elif pion == 2:
                if joueur.pion2 == None:
                    print("ce pion n est pas sur le plateau")
                    self.choix_action_joueur(joueur)
                else:
                    print("choisir la case ou deplacer le pion")
                    x = int(input("x : "))
                    while x>2 or x<0:
                        print("valeur non valide: x = {0, 1, 2}")
                        x = int(input("x : "))
                    y = int(input("y : "))
                    while y>2 or y<0:
                        print("valeur non valide: y = {0, 1, 2}")
                        y = int(input("y : "))
                    if (x==self.plateau.i_none and y==self.plateau.j_none):
                        print("La case est vide, vous ne pouvez pas le deplacer ici")
                        self.choix_action_joueur(joueur)
                    if (self.plateau[x,y].pion != None):
                        print("La case est déjà occupée!")
                        self.choix_action_joueur(joueur)
                    else:
                        self.deplacer_pion(joueur,joueur.pion2,self.plateau[x,y])
            elif pion == 3:
                if joueur.pion3 == None:
                    print("ce pion n est pas sur le plateau")
                    self.choix_action_joueur(joueur)
                else:
                    print("choisir la case ou deplacer le pion")
                    x = int(input("x : "))
                    while x>2 or x<0:
                        print("valeur non valide: x = {0, 1, 2}")
                        x = int(input("x : "))
                    y = int(input("y : "))
                    while y>2 or y<0:
                        print("valeur non valide: y = {0, 1, 2}")
                        y = int(input("y : "))
                    if (x==self.plateau.i_none and y==self.plateau.j_none):
                        print("La case est vide, vous ne pouvez pas le deplacer ici")
                        self.choix_action_joueur(joueur)
                    if (self.plateau[x,y].pion != None):
                        print("La case est déjà occupée!")
                        self.choix_action_joueur(joueur)
                    else:
                        self.deplacer_pion(joueur,joueur.pion3,self.plateau[x,y])
            else:
                print("ce pion n'existe pas")
                self.choix_action_joueur(joueur)
                
        elif choix == 4 and choix4 == True:
            self.double_glissement()
            joueur.glissement_x2=True       #on indique dans la classe joueur qu'il a fait le cout_double
        
        else:
            print("vous ne pouvez pas faire cette action")
            self.choix_action_joueur(joueur)
        
        #si le joueur précédent avait jouer le cout double on remet à false ce cout jouer
        #dans sa classe lui permettant de rejouer ce cout au tour suivant.
        
        if joueur==self.j1:
            if self.j2.glissement_x2==True:
                self.j2.glissement_x2=False
        else:
            if self.j1.glissement_x2==True:
                self.j1.glissement_x2=False

    

        
                
            

        
            
        
                
            
def victoire(joueur,plateau):
        """
        Pour évaluer si un jouer à gagner, on doit définir tous les prédicats menant à la
        victoire, soit tous les façon de gagner
        """
        """victoire : 3 pions sur la 1ere ligne"""
        res = False #on initialise le résultat de la victioreà faux
        #on vérifie que toutes les 3 cases de la 1ere ligne contiennent 3 pions de même couleur
        
        #on ajoute un carre noir ne contenant pas de pion à l'espace vide pour pouvoir effectuer tous les tests
        #on retirera cette ajout pour avoir notre espace vide à la fin du test
        plateau[plateau.i_none,plateau.j_none] = Carre_Noir(plateau.i_none,plateau.j_none)
        
        if (plateau[0,0].pion != None and plateau[0,1].pion != None
            and plateau[0,2].pion != None and plateau[0,0].pion.couleur == 
            plateau[0,1].pion.couleur == plateau[0,2].pion.couleur == joueur.couleur):
                res = True #on renvoit la victoire à True si c'est le cas
            
        #"""victoire : 3 pions sur la 2eme ligne"""
        
        #on vérifie que toutes les 3 cases de la 2eme ligne contiennent 3 pions de même couleur
        if (plateau[1,0].pion != None and plateau[1,1].pion != None
            and plateau[1,2].pion != None and plateau[1,0].pion.couleur == 
            plateau[1,1].pion.couleur == plateau[1,2].pion.couleur == joueur.couleur):
                res = True #on renvoit la victoire à True si c'est le cas
            
        #"""victoire : 3 pions sur la 3eme ligne"""
        
        #on vérifie que toutes les 3 cases de la 3eme ligne contiennent 3 pions de même couleur
        if (plateau[2,0].pion != None and plateau[2,1].pion != None
            and plateau[2,2].pion != None and plateau[2,0].pion.couleur == 
            plateau[2,1].pion.couleur == plateau[2,2].pion.couleur == joueur.couleur):
                res = True #on renvoit la victoire à True si c'est le cas
            
        #"""victoire : 3 pions sur la 1ere colonne"""
        
        #on vérifie que toutes les 3 cases de la 1ere colonne contiennent 3 pions de même couleur
        if (plateau[0,0].pion != None and plateau[1,0].pion != None
            and plateau[2,0].pion != None and plateau[0,0].pion.couleur == 
            plateau[1,0].pion.couleur == plateau[2,0].pion.couleur == joueur.couleur):
                res = True #on renvoit la victoire à True si c'est le cas
            
        #"""victoire : 3 pions sur la 2e colonne"""
        
        #on vérifie que toutes les 3 cases de la 2e colonne contiennent 3 pions de même couleur
        if (plateau[0,1].pion != None and plateau[1,1].pion != None
            and plateau[2,1].pion != None and plateau[0,1].pion.couleur == 
            plateau[1,1].pion.couleur == plateau[2,1].pion.couleur == joueur.couleur):
                res = True #on renvoit la victoire à True si c'est le cas
            
         #"""victoire : 3 pions sur la 3e colonne"""
        
        #on vérifie que toutes les 3 cases de la 3e colonne contiennent 3 pions de même couleur
        if (plateau[0,2].pion != None and plateau[1,2].pion != None
            and plateau[2,2].pion != None and plateau[0,2].pion.couleur == 
            plateau[1,2].pion.couleur == plateau[2,2].pion.couleur == joueur.couleur):
                res = True #on renvoit la victoire à True si c'est le cas
            
         #"""victoire : 3 pions sur la 1ere diagonale"""
        
        #on vérifie que toutes les 3 cases de la 1ere diagonale contiennent 3 pions de même couleur
        if (plateau[0,0].pion != None and plateau[1,1].pion != None
            and plateau[2,2].pion != None and plateau[0,0].pion.couleur == 
            plateau[1,1].pion.couleur == plateau[2,2].pion.couleur == joueur.couleur):
                res = True #on renvoit la victoire à True si c'est le cas
            
        #"""victoire : 3 pions sur la 2eme diagonale"""
        
        #on vérifie que toutes les 3 cases de la 2eme diagonale contiennent 3 pions de même couleur
        if (plateau[2,0].pion != None and plateau[1,1].pion != None
            and plateau[0,2].pion != None and plateau[2,0].pion.couleur == 
            plateau[1,1].pion.couleur == plateau[0,2].pion.couleur == joueur.couleur):
                res = True #on renvoit la victoire à True si c'est le cas
        
        #on retire le carre ajouté pour retrouver l'espace vide initial
        plateau[plateau.i_none,plateau.j_none] = None
        return res #on renvoit la valeur du booléen                
            
##======================================================================
##=======================Fonction éval====================================
##======================================================================   
            
def eval_pion_position(joueur):
        tab_pts= np.array([[3,2,3],[2,4,2],[3,2,3]])
        res = 0
        if joueur.pion1 != None:
            res += tab_pts[joueur.pion1.x,joueur.pion1.y]
        
        if joueur.pion2 != None:
            res += tab_pts[joueur.pion2.x,joueur.pion2.y]
            
        if joueur.pion3 != None:
            res += tab_pts[joueur.pion3.x,joueur.pion3.y]
        
        return res
    
def eval_nb_pions(joueur,plateau):
        nb_pion_joueur=0
        nb_pion_adverse=0
        for i in range(3):
            for j in range(3):
               if plateau[i,j] != None and plateau[i,j].pion != None:
                   if plateau[i,j].pion.couleur == joueur.couleur:
                       nb_pion_joueur+=1
                    
                   else:
                       nb_pion_adverse+=1
                        
        if nb_pion_joueur>nb_pion_adverse:
            return 1
        
        elif nb_pion_joueur<nb_pion_adverse:
            return -1
        
        else:
            return 0    
        
def evaluation(joueur_max,joueur_min,plateau):
        
        if victoire(joueur_max,plateau):
            return 50.
        if victoire(joueur_min,plateau):
            return -50.
        
        else:
            poids1 = eval_pion_position(joueur_max)
            poids1 += eval_nb_pions(joueur_max,plateau)
            return  poids1    
                
##======================================================================#
##=======================Fonction MinMax================================#
##======================================================================# 
            
        
def MaxValue(noeud, profondeur,joueur,autre_joueur):
    if(victoire(joueur,noeud.plateau) or profondeur == 0 ):
        noeud.valeur = evaluation(joueur,autre_joueur,noeud.plateau)
        return evaluation(joueur,autre_joueur,noeud.plateau)
    noeud.valeur = -50.
    for i in range (len(noeud.enfants)):
         
        noeud.valeur = max(noeud.valeur,MinValue(noeud.enfants[i],profondeur-1,joueur,autre_joueur))
    return noeud.valeur


def MinValue(noeud, profondeur,joueur,autre_joueur):
    if(victoire(joueur,noeud.plateau) or profondeur == 0 ):
        noeud.valeur = evaluation(joueur,noeud.autre_joueur,noeud.plateau)
        return evaluation(joueur,autre_joueur,noeud.plateau)
    noeud.valeur = 50.
    for i in range (len(noeud.enfants)):
        
        noeud.valeur = min(noeud.valeur, MaxValue(noeud.enfants[i],profondeur-1,joueur,autre_joueur))
    return noeud.valeur
                
        
def MinMaxPL(noeud,profondeur,joueur,autre_joueur):
    noeud.valeur = MaxValue(noeud,profondeur,joueur,autre_joueur)
    return noeud.valeur 




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
    def __init__(self,profondeur,joueur,autre_joueur,plateau,action_joue = None, valeur = None):
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
        if victoire(self.joueur,self.plateau) != True or victoire(self.autre_joueur,self.plateau) != True:
            
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
# node = Node(3,Joueur("jean","r"),Joueur("pierre","b"),Plateau_jeu())                  
# node.affiche()
# node.enfants[0].affiche()
# node.enfants[0].enfants[0].affiche()
# #node.enfants[0].enfants[0].enfants[0].affiche()
# #node.enfants[0].enfants[0].enfants[8].enfants[16].affiche()  

"""test de la classe jouer"""
"""
P=Plateau_jeu()
j1=Joueur("jean","rouge")
j2=Joueur("pierre","bleu")
jouer=Jouer(P,j1,j2)
jouer.choix_action_joueur(j1)
jouer.plateau.affichePlateau()
jouer.choix_action_joueur(j2)
                        

jouer.poser_pion(j1,P[0,0])
jouer.poser_pion(j2,P[2,1])
jouer.poser_pion(j1,P[2,2])
jouer.deplacer_pion(j1,j1.pion2,P[1,2])
#jouer.plateau.affichePlateau()
jouer.deplacement_glissement(P[0,1])
jouer.plateau.affichePlateau()
print(jouer.plateau.i_none,jouer.plateau.j_none)
jouer.double_glissement()
print(jouer.plateau.i_none,jouer.plateau.j_none)
jouer.plateau.affichePlateau()
jouer.deplacer_pion(j1,j1.pion1,P[0,1])
jouer.plateau.affichePlateau()
jouer.double_glissement()
jouer.deplacer_pion(j1,j1.pion1,P[1,0])
print(jouer.victoire(j1))
jouer.poser_pion(j1,P[1,1])
jouer.plateau.affichePlateau()
print(jouer.victoire(j1))
print(j1.nb_pion,P[0,0].pion)
print(j1.pion1.x,j1.pion1.y,j1.pion1.couleur)
print(j1.pion2.x,j1.pion2.y,j1.pion2.couleur)
print(j2.pion1.x,j2.pion1.y,j2.pion1.couleur)
"""