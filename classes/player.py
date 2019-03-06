#! /usr/bin/env python3
# coding: utf-8


class Player:
    """Class for the character controlled by the player."""

    def __init__(self, position_x, position_y):
        """Player class constructor."""
        self.position_x = position_x  # position sur la largeur
        self.position_y = position_y  # position sur la hauteur
        self.position = (position_x, position_y)
        self.items_collected = 0  # inventaire des items collectés
        self.is_alive = 1  # statut du personnage
