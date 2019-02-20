#! /usr/bin/env python3
# coding: utf-8


""" Module contenant l'ensemble des variables 'standards' du programme."""

# Paramètres de la fenêtre carrée
width_sprite_number = 15  # nombre de cases
height_sprite_number = 15  # nombre de cases
sprite_size = 40  # taille de la case
window_size = width_sprite_number * sprite_size  # taille de la fenetre de jeu

# Personnalisation de la fenêtre
TITLE = "Aidez MacGyver à s'échapper !"
ICON = "../images/MacGyver.png"


# Fichier de la grille du labyrinthe
LABY_FILE = "../map/level.txt"

# Listes des images du jeu
# image_accueil = "../images/graveyard_shift.png"
WIN_PIC = "../images/win_game2.jpg"
LOSE_PIC = '../images/game_lose.jpg'
START = "../images/depart.png"
EXIT = "../images/start.png"
WALL = "../images/wall.jpg"
# wall_list = ["../images/wall_1.png", "../images/wall_2.png", "../images/wall_3.png"]
# WALLS_PIC = random.choice(wall_list)
FLOOR = "../images/floor.jpg"
MAC = '../images/MacGyver.png'
GUARD = "../images/guardian.png"
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