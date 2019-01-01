#! /usr/bin/env python3
# coding: utf-8

import map
import config
import game

class Item:
    """classe qui va gérer les items du jeu"""

    def __init__(self, x_posi, y_posi, picture):  # ajouter "level" aux paramètres ??
        """constructeur de classe"""
        self.position_x = x_posi
        self.position_y = y_posi
        self.picture = picture
        # self.position = []
        self.item_is_on = True
        # self.collected_item()


    def display_item(self):
        """méthode qui affiche graphiquement les items sur la carte"""
        pass



if __name__ == '__main__':
    t = Item(9, 9, config.TUBE)
    print(t.item_is_on)

