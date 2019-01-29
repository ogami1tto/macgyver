#! /usr/bin/env python3
# coding: utf-8

import map
import config


class Item:
    """classe qui va gérer les items du jeu"""

    def __init__(self, position_x, position_y):  # ajouter "level" aux paramètres ??
        """constructeur de classe"""
        self.position_x = position_x
        self.position_y = position_y
        self.position = (position_x, position_y)
        # self.width = width
        # self.height = height
        # self.picture = picture
        # self.position = []
        self.item_is_on = 1
        # self.collected_item()


if __name__ == '__main__':
    t = Item(9, 9)
    print(t.item_is_on)

