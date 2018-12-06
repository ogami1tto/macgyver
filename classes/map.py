#! /usr/bin/env python3
# coding: utf-8

import config  
import character

#! /usr/bin/env python3
# coding: utf-8

class Map:
    """classe qui construit la carte du labyrinthe"""

    def __init__(self):
        """"constructeur de classe"""
        self.level_file = config.LABY_FILE  # fichier texte où se trouve le laby.
        self.map_dict = {}  # dictionnaire où sont stockées les cases du laby.
        self.free_frame = []  # liste contenant les cases vides.
        # self.macgyver = macgyver.Character() # ajouter instance MG à partir de "Character" ?
        # gardien = gardien.Character() # ajouter instance MG à partir de "Character" ?
        self.mg_spawn = []
        self.guardian_spawn = []
        # Character.__init__(self)

    def create_map(self):
        """methode permettant de transformer le fichier texte en un dictionnaire"""
        with open(self.level_file, "r") as level:  # lecture du fichier texte contenant le 'plan' du labyrinthe
            x = 0
            y = 0
            for line in level:
                for char in line:
                    if char != '\n':
                        self.map_dict[
                            str(x), str(y)] = char  # les données du fichier texte sont stockées dans un dictionnaire
                    x += 1
                y += 1
                x = 0

    def mac_spawn(self):
        """methode qui propose de stocker les coordonnées d'apparition de MacGyver"""
        for cle, valeur in self.map_dict.items():
            if valeur == "e":
                self.mg_spawn.append(cle)

    def guard_spawn(self):
        """methode qui propose de stocker les coordonnées d'apparition de MacGyver"""
        for cle, valeur in self.map_dict.items():
            if valeur == "g":
                self.guardian_spawn.append(cle)

    def empty_frame(self):
        """methode qui propose de stocker dans une liste les coordonnées des cases vides du laby"""
        for cle, valeur in self.map_dict.items():
            if valeur == "o":
                self.free_frame.append(cle)

    def map_reader(self, code, exit):
        """methode qui propose de stocker dans une liste les coordonnées des cases vides du laby"""
        self.exit = []
        for cle, valeur in self.map_dict.items():
            if valeur == code:
                exit.append(cle)

    # cette méthode fonctionne, mais en ayant la lettre code en parametre,
    # ca permettrait d'utiliser cette méthode pour déterminer les coordonnées
    # des points de départ des personnages...


if __name__ == '__main__':
    m = Map()
    # print(m.map_dict)
    m.create_map()
    # print(m.map_dict)
    # m.empty_frame()
    # print(m.free_frame)
    m.map_reader("g", "self.free_frame")
    print(m.free_frame)
    # m.guard_spawn()
    # print(m.guardian_spawn)
    # m.mac_spawn()
    # print(m.mg_spawn)


 

    
