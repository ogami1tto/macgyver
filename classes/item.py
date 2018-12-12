#! /usr/bin/env python3
# coding: utf-8


def collected_item():
    # Faire disparaître les items une fois collectés par le personnage !!!
    pass

    # pop_item(self):
    """méthode qui donne la position de l'item dans le laby"""


class Item:
    """classe qui va gérer les items du jeu"""

    def __init__(self, picture):  # ajouter "level" aux paramètres ??
        """constructeur de classe"""
        self.picture = picture
        self.position = []


    def display_item(self):
        """méthode qui affiche graphiquement les items sur la carte"""
        pass


if __name__ == '__main__':
    tube = Item("ok")
