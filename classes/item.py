#! /usr/bin/env python3
# coding: utf-8


class Item:
    """Class for the items to collect in the game."""

    def __init__(self, position_x, position_y):
        """Item class constructor."""
        self.position_x = position_x
        self.position_y = position_y
        self.position = (position_x, position_y)
        self.item_is_on = True
        self.collected = False
