#! /usr/bin/env python3
# coding: utf-8

import map
import config

class Player:
    """classe qui gère le personnage du joueur"""

    def __init__(self, x_posi, y_posi, picture):
        """constructeur de classe"""
        self.position_x = x_posi # position sur la largeur
        self.position_y = y_posi # position sur la hauteur
        self.items_collected = 0 # inventaire des items collectés
        self.picture = picture # image associé au personnage
        self.is_alive = True # statut du personnage
        # self.laby = map.Map()


    # def pick_item(self):
    #     """Methode qui permet de collecter un objet en passant dessus"""
    #     if [self.position_x, self.position_y] == position item:
    #         self.items_collected += 1


    def die_char(self):
        """méthode qui agit sur le statut du personnage"""
        # if position_player == position_guardian and self.items_collected < 3:
        #     self.is_alive = False
        # else:
        #     self.is_alive = True
        pass



if __name__ == '__main__':


    # c = Player(0, 8)
    c = Player(0, 8, config.MAC_PIC)
    print(c.position_x)
    print(c.position_y)

