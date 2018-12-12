#! /usr/bin/env python3
# coding: utf-8

import map


class Player:
    """classe qui gère le personnage du joueur"""
    def __init__(self, x_posi, y_posi):
        """constructeur de classe"""
        self.position_x = x_posi # position sur la largeur
        self.position_y = y_posi # position sur la hauteur
        self.items_collected = 0 # inventaire des items collectés
        # self.start_position_x = map.mcg_spawn[0][0]
        # self.start_position_y = map.mcg_spawn[0][1]

        # self.starting_point = map.mcg_spawn # point de départ sur la map
        # self.status = false or true # statut du personnage
        # self.name = name
        # self.image = MAC_PIC # image associé au personnage
        self.is_alive = True


    def pick_item(self):
        """Methode qui permet de collecter un objet en passant dessus"""
        self.items_collected += 1

    def move_char(self):
        """méthode qui permet d'autoriser les déplacements...
         du personnage dans le labyrinthe"""
        pass

    def die_char(self):
        """méthode qui agit sur le statut du personnage"""
        # if contact guardian and self.items_collected < 3:
        #     self.is_alive = False
        #     else:
        #         self.is_alive = True
        pass





if __name__ == '__main__':
    c = Player(0, 8)
    print(c.position_y)

	# print(c.name)
    # macgyver = Character("mac", 0, 0)
    # print(macgyver.name)
    # print(macgyver.position_y)