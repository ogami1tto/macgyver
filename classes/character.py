#! /usr/bin/env python3
# coding: utf-8

import map

class Character:
    """classe qui gère les personnages"""

# si Mc Gyger sont deux objets de la même classe, doit-on créer des classes 
# fillesnpour chacun d'eux ?
    
    def __init__(self):
        """constructeur de classe"""
        # self.player_controlled = bool(ok)
        # self.starting_point = self.mac_spawn() # point de départ sur la map
        # self.image = picture # image associé au personnage
        # self.status = false or true # statut du personnage  
        self.items_collected = [] # inventaire des items collectés

 
        
    # def spawn_char(self):
        """méthode qui fait apparaître le personnage à un endroit déterminé"""
        # appeler méthode
        # lettre speciale dans les valeurs du dictionnaire LABY_FILE

    def pick_item(self):
    	"""Methode qui permet de collecter un objet en passant dessus"""
        
    def move_char(self):
        """méthode qui permet d'autoriser les déplacements du personnage dans le labyrinthe"""
        
    def die_char(self):
        """méthode qui agit sur le statut du personnage"""


if __name__ == '__main__':
	mcgyver = Character()