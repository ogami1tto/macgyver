#! /usr/bin/env python3
# coding: utf-8

# Faut-il regrouper toutes les classes en un seul fichier ou bien créer des fichiers distincts pour chaque classe ???

class Map:
    """classe qui construit la carte du labyrinthe"""
    
    def __init__(self, level):
        """"constructeur de classe"""
        self.level = level

    def create_map(self):
        """methode permettant de transformer le fichier texte en un dictionnaire"""
        with open(level, "r") as map_file:           # lecture du fichier texte contenant le 'plan' du labyrinthe
            x = 0
            y = 0
            map_dict = {}
            for line in map_file:                    # les données du fichier texte sont stockées dans un dictionnaire
                for char in line:
                    if char != '\n':
                        map_dict[str(x), str(y)] = char
                    x += 1
                y += 1
                x = 0
        
    def display_map():
        """méthode qui génère l'interface graphique à partir du dictionnaire"""
        

 class Item:
    """classe qui va gérer les items du jeu"""
    
    def __init__(self, level):                       # ajouter "level" aux paramètres ??
        """constructeur de classe"""
        
    def random_item(self):
        """méthode qui place aléatoire les différents items sur la carte"""
        
    def display_item(self):
        """méthode qui affiche graphiquement les items sur la carte"""
                                                     # Le Gardien est-il considéré comme un item ???
                                                     # Faire disparaître les items une fois collectés par le personnage !!!
        
        
 class Character:
    """classe qui gère le personnage contrôlé par le joueur"""
    
    def __init__(self, level):                       # ajouter "level" aux paramètres ??
        """constructeur de classe"""
        
    def spawn_char(self):
        """méthode qui fait apparaître le personnage à un endroit déterminé"""
        
    def move_char(self):
        """méthode qui permet d'autoriser les déplacements du personnage dans le labyrinthe"""
        
    def display_char(self):
        """méthode qui affiche graphiquement le personnage sur la carte"""
        
    
    
