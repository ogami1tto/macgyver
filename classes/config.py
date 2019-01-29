#! /usr/bin/env python3
# coding: utf-8

import random

""" Module contenant l'ensemble des variables 'standards' du programme."""

# Paramètres de la fenêtre carrée
sprite_number = 15  # nombre de cases
sprite_size = 40  # taille de la case
window_size = sprite_number * sprite_size  # taille de la fenetre de jeu

# Personnalisation de la fenêtre
TITLE = "Aidez MacGyver à s'échapper !"
# ICON = "../images/MacGyver.bmp"
ICON = "../images/MacGyver.png"


# Fichier de la grille du labyrinthe
LABY_FILE = "../map/level.txt"

# Listes des images du jeu
# image_accueil = "../images/graveyard_shift.png"
BACKGROUND_PIC = "../images/operation_stealth.png"
START = "../images/depart.png"
EXIT = "../images/exit.png"
WALL_PIC = "../images/wall.jpg"
# wall_list = ["../images/wall_1.png", "../images/wall_2.png", "../images/wall_3.png"]
# WALLS_PIC = random.choice(wall_list)
FLOOR_PIC = "../images/floor.jpg"
MAC_PIC = '../images/MacGyver.png'
MURD_PIC = "../images/guardian.png"
ETHER = "../images/ether.png"
TUBE = "../images/tube.png"
NEEDLE = "../images/needle.png"
titre_fenetre = "MacGyver Labyrinthe"

# image_accueil = "../images/operation_stealth.bmp"
# BACKGROUND_PIC = "../images/operation_stealth.bmp"
# START = "../images/depart.png"
# EXIT = "../images/floor.bmp"
# WALL_PIC = "../images/wall-tiles.bmp"
# FLOOR_PIC = "../images/floor.bmp"
# MAC_PIC = '../images/MacGyver.bmp'
# MURD_PIC = "../images/guardian.bmp"
# ETHER = "../images/ether.bmp"
# TUBE = "../images/tube.bmp"
# NEEDLE = "../images/needle.bmp"
# titre_fenetre = "MacGyver Labyrinthe"