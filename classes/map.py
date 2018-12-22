#! /usr/bin/env python3
# coding: utf-8

import random
import config
import player
import guardian
import item
import position

class Map:
    """classe qui construit la carte du labyrinthe"""

    def __init__(self):
        """"constructeur de classe"""
        self.map_full = {} # dictionnaire où sont stockées les cases du laby.
        self.laby_x = config.LABY_WIDTH # largeur du labyrinthe
        self.laby_y = config.LABY_HEIGHT # hauteur du labyrinthe
        self.free_frame = []  # liste contenant les cases vides.
        self.wall = [] # liste contenant les cases 'mur'.
        self.items = [] # liste contenant les items.
        self.mcg_spawn = [] # coordonnees apparition MacGyver
        self.guardian_spawn = [] # coordonnees apparition du Gardien

        self.create_map() # lance la méthode création du laby à partir du fichier .txt
        self.map_reader() # lance la méthode interprétation du fichier .txt
        self.random_items() # lance la méthode
        # self.position_guardian = position.Position(self.guardian_spawn[0][0], self.guardian_spawn[0][1])
        # self.test()

        """creer instance pour MacGyver, le Gardien, et les items"""
        self.macgyver = player.Player(self.mcg_spawn[0][0], self.mcg_spawn[0][1])
        self.murdock = guardian.Guardian(self.guardian_spawn[0][0], self.guardian_spawn[0][1])
        self.item_1 = item.Item(self.items[0][0], self.items[0][1])
        self.item_2 = item.Item(self.items[1][0], self.items[1][1])
        self.item_3 = item.Item(self.items[2][0], self.items[2][1])


    def create_map(self):
        """methode permettant de transformer le fichier texte en un dictionnaire"""
        with open(config.LABY_FILE, "r") as level:  # lecture du fichier texte
                                                    # contenant le 'plan' du
                                                    # labyrinthe
            x = 0
            y = 0
            for line in level:
                for char in line:
                    if char != '\n':
                        self.map_full[str(x), str(y)] = char  # les données du
                                                              # fichier texte sont
                                                              # stockées dans un dictionnaire
                    x += 1
                y += 1
                x = 0


    def map_reader(self):
        """methode qui propose de stocker dans une liste...
         les coordonnées de cases d'un type à spécifier"""
        for cle, valeur in self.map_full.items():
            if valeur == "m":
                self.mcg_spawn.append(cle)
            elif valeur == "g":
                self.guardian_spawn.append(cle)
            elif valeur == "o":
                self.free_frame.append(cle)
            elif valeur == "x":
                self.wall.append(cle)


    def random_items(self):
        """methode qui choisit au hasard 3 emplacements pour les items"""
        self.items = random.sample(self.free_frame, 3)


    def display_laby(self):
        self.wall = WALLS_PIC
        self.floor = FLOOR_PIC


    # def test(self):
    #     return self.murdock.position_y


if __name__ == '__main__':
    m = Map()
    print(m.mcg_spawn)
    print(m.mcg_spawn[0][0])
    print(m.mcg_spawn[0][1])
    print(m.macgyver.position_x)
    print(m.macgyver.position_y)
    # print(m.macgyver.position_y)
    # print(m.guardian_spawn)
    print(m.murdock.is_alive)
    # print(m.position_guardian)
    print(m.guardian_spawn)
    print(m.murdock.position_x)
    print(m.murdock.position_y)
    # print(m.items)
    # print(m.item_1.position_x)
    # print(m.item_3.position_y)
    # print(test())











