#! /usr/bin/env python3
# coding: utf-8


class Item:
    """classe qui va gérer les items du jeu"""

    def __init__(self, position_x, position_y):
        """constructeur de classe"""
        self.position_x = position_x
        self.position_y = position_y
        self.position = (position_x, position_y)
        self.item_is_on = True
        self.collected = False


if __name__ == '__main__':
    t = Item(9, 9)
    print(t.item_is_on)
