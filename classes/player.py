#! /usr/bin/env python3
# coding: utf-8

import map
import config
import item

class Player:
    """classe qui gère le personnage du joueur"""

    def __init__(self, position_x, position_y):
        """constructeur de classe"""
        self.position_x = position_x # position sur la largeur
        self.position_y = position_y # position sur la hauteur
        self.position = (position_x, position_y)
        # self.width = width
        # self.height = height
        # self.items_collected = 0 # inventaire des items collectés
        # self.picture = picture # image associé au personnage
        # self.is_alive = True # statut du personnage


if __name__ == '__main__':


    c = Player(0, 8)
    print(c.position_x)
    print(c.position_y)

