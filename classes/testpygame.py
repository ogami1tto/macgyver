#! /usr/bin/env python3
# coding: utf-8

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame
from pygame.locals import *

import map
import config
import player
import guardian
import item
from config import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((window_size, window_size))
#Icone
icone = pygame.image.load(MAC_PIC)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)


#BOUCLE PRINCIPALE
continuer = 1
while continuer:
    #Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))

    #Rafraichissement
    pygame.display.flip()

    #On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1

    #BOUCLE D'ACCUEIL
    while continuer_accueil:

        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            #Si l'utilisateur quitte, on met les variables
            #de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = 0
                continuer_jeu = 0
                continuer = 0
                #Variable de choix du niveau
                choix = 0

            elif event.type == KEYDOWN:
                #Lancement du niveau 1
                if event.key == K_F1:
                    continuer_accueil = 0   #On quitte l'accueil
                    choix = 'n1'        #On définit le niveau à charger
                #Lancement du niveau 2
                elif event.key == K_F2:
                    continuer_accueil = 0
                    choix = 'n2'



    #on vérifie que le joueur a bien fait un choix de niveau
    #pour ne pas charger s'il quitte
    if choix != 0:
        #Chargement du fond
        fond = pygame.image.load(operation_stealth).convert()

        #Génération d'un niveau à partir d'un fichier
        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(fenetre)

        #Création de Donkey Kong
        dk = Perso("images/mac_right.png", "images/mac_left.png",
        "images/mac_up.png", "images/mac_down.png", niveau)


    #BOUCLE DE JEU
    while continuer_jeu:

        #Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            #Si l'utilisateur quitte, on met la variable qui continue le jeu
            #ET la variable générale à 0 pour fermer la fenêtre
            if event.type == QUIT:
                continuer_jeu = 0
                continuer = 0

            elif event.type == KEYDOWN:
                #Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.key == K_ESCAPE:
                    continuer_jeu = 0

                #Touches de déplacement de Donkey Kong
                elif event.key == K_RIGHT:
                    dk.deplacer('droite')
                elif event.key == K_LEFT:
                    dk.deplacer('gauche')
                elif event.key == K_UP:
                    dk.deplacer('haut')
                elif event.key == K_DOWN:
                    dk.deplacer('bas')

        #Affichages aux nouvelles positions
        fenetre.blit(fond, (0,0))
        niveau.afficher(fenetre)
        fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
        pygame.display.flip()

        #Victoire -> Retour à l'accueil
        if niveau.structure[dk.case_y][dk.case_x] == 'a':
            continuer_jeu = 0




# #Importation des bibliothèques nécessaires
# from pygame import *

# #Initialisation de la bibliothèque Pygame
# pygame.init()

# #Création de la fenêtre
# fenetre = pygame.display.set_mode((640, 480))

# #Variable qui continue la boucle si = 1, stoppe si = 0
# continuer = 1

# #Boucle infinie
# while continuer:
#     continue #Je place continue ici pour pouvoir relancer la boucle infinie
#                  #mais il est d'habitude remplacé par une suite d'instructions




# class Laby:
#     # X
#     # Y
#     # 1 => SOL | 2 => MUR
#     # Item...
#     # etc...
#     Coordonnees = [
#     []*100,
#     []*100,
#     []*100
#     ]

#     def MethodeIncrementTest(self, test):
#         test += 1
#         return test

#     def ChargeLaby(self):
#         Coordonnees = [
#     [0]*100,
#     [0]*100,
#     [0]*100,
#     ]
#         d = sorted(Coordonnees)
#         d[0][0] = 1 # x
#         d[1][0] = 1 # y
#         d[2][0] = 1 # type de sol
#         return d

# if __name__ == '__main__':

#     test = 0
#     Coordonnees = [
#     []*100,
#     []*100,
#     []*100
#     ]
#     test = Laby.MethodeIncrementTest()
#     Coordonnees = Laby.ChargeLaby(Coordonnees)

#     print(Coordonnees)
