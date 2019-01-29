#! /usr/bin/env python3
# coding: utf-8

import map
import config

class Guardian:
    """classe qui gère le gardien"""

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.position = (position_x, position_y)
        # self.height = height
        # self.width = width
        # self.picture = picture
        self.is_alive = 1 # statut du personnage
        # self.image = MURD_PIC # image associé au personnage


if __name__ == '__main__':
    c = Guardian(0, 6)
    print(c.position)

