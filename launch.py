#! /usr/bin/env python3
# coding: utf-8

"""
Jeu Labyrinthe MacGyver
Jeu dans lequel on doit déplacer MacGyver jusqu'à la sortie au travers d'un labyrinthe.
Script Python
Fichiers : config.py, game.py, guardian.py, item.py, map.py, player.py, position.py, map + images
"""


from classes import game


def main():
    new_game = Game()
    new_game.run_pygame()


if __name__ == "__main__":
    main()