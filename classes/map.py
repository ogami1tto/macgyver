#! /usr/bin/env python3
# coding: utf-8

import config  
import character

class Map:
    """classe qui construit la carte du labyrinthe"""
    
    def __init__(self):
        """"constructeur de classe"""
        self.level_file = config.LABY_FILE  # fichier texte où se trouve le laby.
        self.map_dict = {}    # dictionnaire où sont stockées les cases du laby.
        self.free_frame = []  # liste contenant les cases vides.
        mcgyver = Character()

    def create_map(self):
        """methode permettant de transformer le fichier texte en un dictionnaire"""
        with open(self.level_file, "r") as level:    # lecture du fichier texte contenant le 'plan' du labyrinthe
            x = 0
            y = 0
            for line in level:                       
                for char in line:
                    if char != '\n':
                        self.map_dict[str(x), str(y)] = char # les données du fichier texte sont stockées dans un dictionnaire
                    x += 1
                y += 1
                x = 0


    def empty_frame(self):
        """methode qui propose de stocker dans une liste les coordonnées des cases vides du laby"""
        for cle, valeur in self.map_dict.items():
            if valeur == "o":
                self.free_frame.append(cle)



if __name__ == '__main__':
    m = Map()
    # print(m.map_dict)
    m.create_map()
    # print(m.map_dict)
    m.empty_frame()
    print(m.free_frame)


 

    
