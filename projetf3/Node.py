# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:08:45 2020

@author: fabie et jeoffrey
"""

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
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        