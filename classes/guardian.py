#! /usr/bin/env python3
# coding: utf-8


class Guardian:
    """Class for the guardian protecting the exit in the game."""

    def __init__(self, position_x, position_y):
        """Class constructor."""
        self.position_x = position_x
        self.position_y = position_y
        self.position = (position_x, position_y)
        self.is_alive = 1
