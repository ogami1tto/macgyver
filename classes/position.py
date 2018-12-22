#! /usr/bin/env python3
# coding: utf-8

import map

class Position:
    """classe qui gère les positions de tous les objets"""

    def __init__(self, x_posi, y_posi):
        """constructeur de classe"""
        self.position_x = x_posi # position sur la largeur
        self.position_y = y_posi # position sur la hauteur



if __name__ == '__main__':
    s = Position(0,7)
    print(s.position_y)

