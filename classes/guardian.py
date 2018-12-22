#! /usr/bin/env python3
# coding: utf-8

import map
import config

class Guardian:
    """classe qui gère le gardien"""

    def __init__(self, x_posi, y_posi, picture):
        self.position_x = x_posi
        self.position_y = y_posi
        self.picture = picture
        self.is_alive = True # statut du personnage

        # self.image = MURD_PIC # image associé au personnage


if __name__ == '__main__':
    c = Guardian(0, 6, config.MURD_PIC)
    print(c.position_y)
