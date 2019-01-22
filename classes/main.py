#! /usr/bin/env python3.5
# coding: utf-8

"""
Jeu Labyrinthe MacGyver
Jeu dans lequel on doit déplacer MacGyver jusqu'à la sortie au travers d'un labyrinthe.

Script Python
Fichiers : config.py, game.py, guardian.py, item.py, map.py, player.py, position.py, map + images
"""

import pygame
from pygame.locals import *
import map
import config
import player
import guardian
import item
import game

# Pygame initialization
pygame.init()

#Pygame window display
window = pygame.display.set_mode((config.window_size, 600))

#Icon
# icon = pygame.image.load("images/perso.png")
# icon = pygame.image.load(config.MAC_PIC).convert_alpha()
# pygame.display.set_icon(config.ICON)

#Title
pygame.display.set_caption(config.TITLE)

#Background display
# background_tiles = pygame.image.load(config.BACKGROUND_PIC).convert()
# Window.blit(background_tiles, (30, 30))  # the background is streched from below
                                         # the black margin to the opposite corner
""" displaying the character .png"""
# Char_img = pygame.image.load(config.MAC_PIC).convert_alpha()  # Add the png and transparency

""" displaying the walls of the maze"""
# wall = pygame.image.load(config.WALL_PIC).convert()

""" displaying the objects png's"""
# tubeIMG = pygame.image.load(config.TUBE).convert_alpha()
# needleIMG = pygame.image.load(config.NEEDLE).convert_alpha()
# etherIMG = pygame.image.load(config.ETHER).convert_alpha()

# refreshing the screen for the background to be visible over the default one
pygame.display.flip()

# Variable for the infinite loop
game_loop = 1

# Variables to check if the items have been picked or not:
TubeNotPicked = True
EtherNotPicked = True
NeedleNotPicked = True

GAME_WON = False
GAME_LOOSE = False

pygame.key.set_repeat(400, 30)  #Moving MaGyver by maintening a arrow_key pressed

game = game.Game()


#BOUCLE DE JEU
while game_loop:

    #Limitation de vitesse de la boucle
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():

        #Si l'utilisateur quitte, on met la variable qui continue le jeu
        #ET la variable générale à 0 pour fermer la fenêtre
        if event.type == QUIT:
            game_loop = 0

        elif event.type == KEYDOWN:
            #Si l'utilisateur presse Echap ici, on revient seulement au menu
            if event.key == K_ESCAPE:
                game_loop = 0



    #Affichages aux nouvelles positions
       pygame.display.flip()


    #Victoire -> Retour à l'accueil
    if game.grid[int(game.position_x), int(game.position_y)] == "s":
    # if level.structure[Mac.case_y][Mac.case_x] == 'a':  # If MacGyver reach the guard :
        if TubeNotPicked is False and NeedleNotPicked is False and EtherNotPicked is False:  # If every objects have been looted, he won.
            GAME_WON = True
        else:
            GAME_OVER = True  # Else it's game over !



    if GAME_WON is True:
        window.blit(Background_Tiles, (0, 30))  # draw over everything on the screen now by re-drawing the background
        font = pygame.font.Font(None, 25)
        text = font.render("You won ! MacGyver is safe thanks to you !", 1, (255, 255, 255)) # Display the text in white with rounded edge
        textrect = text.get_rect()
        textrect.centerx, textrect.centery = Window_Size / 2, Window_Size / 2  # Centering the text 
        window.blit(text, textrect)

        pygame.display.flip()

    if GAME_LOOSE is True:
        window.blit(Background_Tiles, (0, 30))  # draw over everything on the screen now by re-drawing the background
        font = pygame.font.Font(None, 25)
        text = font.render("Game over! You just died.", 1, (255, 255, 255))  # Display the text in white with rounded edge
        textrect = text.get_rect()
        textrect.centerx, textrect.centery = window_size / 2, window_size / 2
        window.blit(text, textrect)

        pygame.display.flip()





