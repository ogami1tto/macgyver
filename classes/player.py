#! /usr/bin/env python3
# coding: utf-8

import map
import config
import item

class Player:
    """classe qui gère le personnage du joueur"""

    def __init__(self, x_posi, y_posi, width, height):
        """constructeur de classe"""
        self.position_x = x_posi # position sur la largeur
        self.position_y = y_posi # position sur la hauteur
        self.width = width
        self.height = height
        # self.items_collected = 0 # inventaire des items collectés
        # self.picture = picture # image associé au personnage
        # self.is_alive = True # statut du personnage



if __name__ == '__main__':


    # c = Player(0, 8)
    c = Player(0, 8, config.MAC_PIC)
    print(c.position_x)
    print(c.position_y)

