# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:56:50 2020

@author: jeome
"""

from Pion import Pion
from Carre_Noir import Carre_Noir
from Joueur import Joueur
from Plateau_Jeu import Plateau_jeu
from Jouer import Jouer

nom_j1 = input("entrez le nom du joueur 1 : ")
couleur_j1 = input("entrez la couleur du joueur 1 : ")
nom_j2 = input("entrez le nom du joueur 2 : ")
couleur_j2 = input("entrez la couleur du joueur 2 : ")

j1 = Joueur(nom_j1,couleur_j1)
j2 = Joueur(nom_j2,couleur_j2)
plateau = Plateau_jeu()
jouer = Jouer(plateau, j1, j2)
res = False
resj2 = False
gagnant = ''

while res == False:
    jouer.plateau.affichePlateau()
    jouer.choix_action_joueur(j1)
    gagnant = j1.nom
    resj1=jouer.victoire(j1)
    
    if resj1 == True:
        res=True
    else:
        jouer.plateau.affichePlateau()
        jouer.choix_action_joueur(j2)
        gagnant = j2.nom
        resj2=jouer.victoire(j2)
       
        if resj2 == True:
            res=True
    
print("Bravo, ",gagnant,"à gagner")