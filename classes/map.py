#! /usr/bin/env python3
# coding: utf-8

import config  

class Map:
    """classe qui construit la carte du labyrinthe"""
    
    def __init__(self):
        """"constructeur de classe"""
        self.level_file = config.LABY_FILE
        self.map_dict = {}

    def create_map(self):
        """methode permettant de transformer le fichier texte en un dictionnaire"""
        with open(self.level_file, "r") as level:           # lecture du fichier texte contenant le 'plan' du labyrinthe
            x = 0
            y = 0
            for line in level:                    # les données du fichier texte sont stockées dans un dictionnaire
                for char in line:
                    if char != '\n':
                        self.map_dict[str(x), str(y)] = char
                    x += 1
                y += 1
                x = 0


if __name__ == '__main__':
    m = Map()
    print(m.map_dict)
    m.create_map()
    print(m.map_dict)



    # def display_map():
    #     """méthode qui génère l'interface graphique à partir du dictionnaire"""
        

 

    
