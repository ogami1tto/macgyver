#! /usr/bin/env python3
# coding: utf-8


class Player:
    """classe qui gère le personnage du joueur"""

    def __init__(self, position_x, position_y):
        """constructeur de classe"""
        self.position_x = position_x  # position sur la largeur
        self.position_y = position_y  # position sur la hauteur
        self.position = (position_x, position_y)
        self.items_collected = 0  # inventaire des items collectés


if __name__ == '__main__':
    c = Player(0, 8)
    print(c.position_x)
    print(c.position_y)
