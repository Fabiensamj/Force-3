# -*- coding: utf-8 -*-
#
# Fichier générant une partie du jeu FORCE 3
#
# Ce fichier est appelé par le fichier Accueil.py
#
# Ce fichier créé une partie permettant à l'utilisateur de jouer sur plusieurs modes:
#
#       Joueur contre Joueur || Joueur contre le robot || Robot contre Robot
#
from Plateau_Jeu import Pion
from Plateau_Jeu import Carre_Noir
from Plateau_Jeu import Joueur
from Plateau_Jeu import Plateau_jeu
from Jouer import Jouer
from Jouer import victoire

#================================================================================================#
#=====================Fonction qui crée la partie Robot contre robot=============================#
#================================================================================================#

def iaVSia():
    nom_j1 = "Bot rouge"
    couleur_j1 = "rouge"
    nom_j2 = "Bot bleu"
    couleur_j2 = "bleu"

# Création des joueurs
    j1 = Joueur(nom_j1,couleur_j1)
    j2 = Joueur(nom_j2,couleur_j2)
#=======
    plateau = Plateau_jeu() # Initialisation du plateau de jeu
    jouer = Jouer(plateau, j1, j2)
    res = False

    gagnant = ''

    while res == False:
        jouer.plateau.affichePlateau()          #
        jouer.choix_action_ia(j1)               # Actions Joueur 1
        gagnant = j1.nom                        #
        resj1=victoire(j1,jouer.plateau)        #
    
    
        if resj1 == True:                       #vérification de la condition de victoire
            res=True
        else:
            jouer.plateau.affichePlateau()      #
            jouer.choix_action_ia(j2)           # Actions Joueur 2
            gagnant = j2.nom                    #
            resj2=victoire(j2,jouer.plateau)    #
       
        if resj2 == True:                       #vérification de la condition de victoire
            res=True
         
    jouer.plateau.affichePlateau()
    if (victoire(j2,jouer.plateau) and victoire(j1,jouer.plateau)):
        print("Egalité")
    else:
        print("Bravo, ",gagnant,"à gagner")

#================================================================================================#
#=====================Fonction qui crée la partie Joueur contre robot============================#
#================================================================================================#
    
def jVSia():
    nom_j1 = input("entrez le nom du joueur 1 : ")
    couleur_j1 = "rouge"
    nom_j2 = "Bot bleu"
    couleur_j2 = "bleu"

    j1 = Joueur(nom_j1,couleur_j1)
    j2 = Joueur(nom_j2,couleur_j2)
    plateau = Plateau_jeu()
    jouer = Jouer(plateau, j1, j2)
    res = False

    gagnant = ''

    while res == False:
        jouer.plateau.affichePlateau()          # 
        jouer.choix_action_joueur(j1)           # Actions Joueur 1
        gagnant = j1.nom                        # 
        resj1=victoire(j1,jouer.plateau)        # 
    
    
        if resj1 == True:
            res=True
        else:
            jouer.plateau.affichePlateau()      # 
            jouer.choix_action_ia(j2)           # Actions Joueur 2
            gagnant = j2.nom                    # 
            resj2=victoire(j2,jouer.plateau)    # 
       
        if resj2 == True:
            res=True
            
    jouer.plateau.affichePlateau()
    if (victoire(j2,jouer.plateau) and victoire(j1,jouer.plateau)):
        print("Egalité")
    else:
        print("Bravo, ",gagnant,"à gagner")

#================================================================================================#
#=====================Fonction qui crée la partie Joueur contre Joueur===========================#
#================================================================================================#
    
def jVSj():
    nom_j1 = input("entrez le nom du joueur 1 : ")
    couleur_j1 = "rouge"
    nom_j2 = input("entrez le nom du joueur 1 : ")
    couleur_j2 = "bleu"

    j1 = Joueur(nom_j1,couleur_j1)
    j2 = Joueur(nom_j2,couleur_j2)
    plateau = Plateau_jeu()
    jouer = Jouer(plateau, j1, j2)
    res = False

    gagnant = ''

    while res == False:
        jouer.plateau.affichePlateau() 
        jouer.choix_action_joueur(j1)
        gagnant = j1.nom
        resj1=victoire(j1,jouer.plateau)
    
    
        if resj1 == True:
            res=True
        else:
            jouer.plateau.affichePlateau()
            jouer.choix_action_joueur(j2)
            gagnant = j2.nom
            resj2=victoire(j2,jouer.plateau)
       
        if resj2 == True:
            res=True
            
    jouer.plateau.affichePlateau()
    if (victoire(j2,jouer.plateau) and victoire(j1,jouer.plateau)):
        print("Egalité")
    else:
        print("Bravo, ",gagnant,"à gagner")



   
