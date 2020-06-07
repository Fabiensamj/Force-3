# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 14:56:50 2020

@author: jeome
"""

from Plateau_Jeu import Pion
from Plateau_Jeu import Carre_Noir
from Plateau_Jeu import Joueur
from Plateau_Jeu import Plateau_jeu
from Jouer import Jouer
from Jouer import victoire


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
    jouer.choix_action_ia(j1)
    gagnant = j1.nom
    resj1=victoire(j1,jouer.plateau)
    
    
    if resj1 == True:
        res=True
    else:
        jouer.plateau.affichePlateau()
        jouer.choix_action_ia(j2)
        gagnant = j2.nom
        resj2=victoire(j2,jouer.plateau)
       
        if resj2 == True:
            res=True
    
print("Bravo, ",gagnant,"à gagner")