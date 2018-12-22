#! /usr/bin/env python3
# coding: utf-8

import map
import config

class Item:
    """classe qui va gérer les items du jeu"""

    def __init__(self, x_posi, y_posi, picture):  # ajouter "level" aux paramètres ??
        """constructeur de classe"""
        self.position_x = x_posi
        self.position_y = y_posi
        self.picture = picture
        # self.position = []
        self.item_is_on = True


    def display_item(self):
        """méthode qui affiche graphiquement les items sur la carte"""
        pass


    def collected_item():
        # Faire disparaître les items une fois collectés par le personnage !!!
        # if position item == position player:
        #     self.item_is_on = False
        # else:
        #     True
        #     while player(position) not item(position):
        # self.item_is_on = True
        pass


if __name__ == '__main__':
    t = Item(9, 9, config.TUBE)

