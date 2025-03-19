# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 08:41:16 2023

@author: valorle
"""

import matplotlib.pyplot as plt
import random

########################################
# Carte
########################################
class Carte:
    def __init__(self, figure, couleur, valeur):
        self.figure     = figure
        self.couleur    = couleur
        self.valeur     = valeur
        
    def __str__(self):
        return "{} de {} : valeur {}".format(self.figure.upper(), self.couleur.upper(), self.valeur)
        
    # afficher une seule carte
    def plot(self, axes=None):
        # import img
        if self.valeur < 10: # pour les cartes de 1 a 9
            imgNom = "cartes/test-0{}-{}-img.png".format(self.valeur, self.couleur.lower());
        else: # pour les cartes 10, valet, dame et roi
            fig = self.figure.upper()
            options = {'10'     : '10',
                       'VALET'  : 'V',
                       'DAME'   : 'D',
                       'ROI'    : 'R'};
            imgNom = "cartes/test-{}-{}-img.png".format(options[fig], self.couleur.lower());
        img = plt.imread(imgNom)
        # set axes
        if axes is not None:
            axes.axes.clear() 
            imgplot = axes.imshow(img) 
            axes.axis('off') 
        else: 
            plt.clf()
            imgplot = plt.imshow(img) 
            plt.axis('off')
        return imgplot
    
    
    
########################################
# PaquetCartes
######################################## 
class PaquetCartes:
    # creer un paquet vide de cartes
    def __init__(self):
        self.listeCartesDuPaquet = [] 
        
    # imprimer toutes les cartes dans le paquet
    def __str__(self):
        return "\n".join(c.__str__() for c in self.listeCartesDuPaquet)
    
    # retourner le longueur de la liste des cartes (nombre )
    def __len__(self):
        return len(self.listeCartesDuPaquet)
    
    # melanger toutes les cartes dans ce paquet
    def melanger(self):
        random.shuffle(self.listeCartesDuPaquet);
        
    # supprimer la premiere carte de ce paquet
    def tirerCarte(self):
        if self.listeCartesDuPaquet is not None:
            carteRetire = self.listeCartesDuPaquet[0]
            self.listeCartesDuPaquet.remove(self.listeCartesDuPaquet[0]);
            return carteRetire;
        else:
            return None;
    
    # ajouter la carte a la fin de ce paquet
    def ajouterCarteDansPaquet(self, carte):
        self.listeCartesDuPaquet.append(carte)
        
    # retourner la somme des valeurs de ce paquet
    def getValeurDuPaquet(self):
        val = 0;
        for c in self.listeCartesDuPaquet:
            val += c.valeur;
        return val;
    
    # supprimer toutes les cartes
    def clearPaquet(self):
        for c in self.listeCartesDuPaquet:
            c.remove()
    
    
    def plot(self,fig=None,left=0,bottom=0,width=0.2,height=0.2,shift=0.05): 
        # affiche l'ensemble des cartes du paquet en les décalant 
        if fig == None: fig=plt.figure() 
        for c in self.listeCartesDuPaquet: 
            axes=fig.add_axes([left,bottom,width,height]) 
            c.plot(axes) 
            left+=shift 
            if left >0.9: 
                left=0 
                bottom +=0.15



########################################
# JeuCartesBlackJack
######################################## 
class JeuCartesBlackJack:
    def __init__(self, N):
        self.jeuCartesEnsemble = PaquetCartes()
        carteFigure     = ('as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi')
        carteCouleur    = ('Carreau', 'Coeur', 'Pique', 'Trefle')
        carteValeur     = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
        i = 0
        m = 0
        n = 0
        for i in range(0,N): # loop de nombre de paquets de 52 cartes utilises
            for m in range(0,4): # loop de couleur
                for n in range(0,13): # loop de figure et valeur
                    self.jeuCartesEnsemble.ajouterCarteDansPaquet(Carte(carteFigure[n], carteCouleur[m], carteValeur[n]))
                    # print(Carte(carteFigure[n], carteCouleur[m], carteValeur[n]))
        self.jeuCartesEnsemble.melanger() # melanger les cartes
        print('Il y a {} de cartes dans ce jeu.'.format(len(self.jeuCartesEnsemble))) # verifier le nombre des cartes
        
    # afficher toutes les cartes dans le jeu cartes Black Jack
    def plot(self):
        self.jeuCartesEnsemble.plot()
        
# class CarteCouleur(Enum):
#     CARREAU = 1
#     COEUR   = 2
#     PIQUE   = 3
#     TREFLE  = 4

if __name__ == '__main__':
    C = Carte('as','pique',1)
    print(C)
    # C.plot()
    
    C1 = Carte('as','pique',1) 
    C2 = Carte('as','coeur',1) 
    C3 = Carte('Valet','Trefle',10) 
    C4 = Carte('3','Pique',3)
    P = PaquetCartes() 
    P.ajouterCarteDansPaquet(C1) 
    P.ajouterCarteDansPaquet(C2) 
    P.ajouterCarteDansPaquet(C3) 
    P.ajouterCarteDansPaquet(C4) 
    print('Le paquet contient {} cartes et sa valeur est {}'.format(len(P),P.getValeurDuPaquet())) 
    print(P) 
    carte=P.tirerCarte() 
    print('Le {} a été retiré du paquet'.format(carte))
    P.plot()
    
    jeu=JeuCartesBlackJack(2) # creation d’un jeu de black Jack à partir de 2 jeux de 52 cartes 
    jeu.plot() # afficher
    
class Joueur:
    def __init__(self,prenom,argent,mise,etat,paquetJoueur):
        self.prenom=prenom
        self.argent=argent
        self.mise=mise
        self.etat=etat
        self.paquetJoueur=paquetJoueur
        
    def __str__(self):
        return f"Joueur: {self.prenom},argent:{self.argent}, etat: {self.etat}"

    ef __str__(self):
        return f"{self.prenom}, Argent: {self.argent}, Mise: {self.mise}, Etat: {self.etat}"

    def setEtatJoueur(self, nouvelEtat):
        if nouvelEtat in ['run', 'stop', 'perdu', 'inactif', 'gagne']:
            self.etat = nouvelEtat
        else:
            raise ValueError("Etat non autorisé")

    def ajouterCarteDansPaquetJoueur(self, carte):
        self.paquetJoueur.append(carte)

    def addArgentJoueur(self, argent):
        self.argent += argent

    def clearPaquetJoueur(self):
        self.paquetJoueur = []

    def miseJoueur(self, miseMin):
        mise = int(input("Combien voulez-vous miser ? "))
        if mise >= miseMin and mise <= self.argent:
            self.mise = mise
            return mise
        else:
            print(f"La mise doit être entre {miseMin} et {self.argent}")
            return 0

    def action(self):
        action = input("Quelle action souhaitez-vous faire ? (tirer: 1 ou 2 cartes, p: passer, s: arrêter) ")
        if action in ['1', '2', 'p', 's']:
            return action
        else:
            print("Action non autorisée")
            return None
    
    if __name__ == '__main__':
        j1=joueur('obelix',100)
        j1.ajout
        
        
    
