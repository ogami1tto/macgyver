#! /usr/bin/env python3
# coding: utf-8


class Item:
    """classe qui va gérer les items du jeu"""
    
    def __init__(self, picture):                       # ajouter "level" aux paramètres ??
        """constructeur de classe"""
        # self.picture = picture
        # self.position = []

        
    def random_item(self):
        """méthode qui place aléatoire les différents items sur la carte"""
        pass
        
    def display_item(self):
        """méthode qui affiche graphiquement les items sur la carte"""
        pass
    
    def collected_item(self):
    # Faire disparaître les items une fois collectés par le personnage !!!
        pass

        
    # pop_item(self):
        """méthode qui donne la position de l'item dans le laby"""



if __name__ == '__main__':
	tube = Item()