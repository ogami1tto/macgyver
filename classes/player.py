#! /usr/bin/env python3
# coding: utf-8

import map
import position

class Player:
    """classe qui gère le personnage du joueur"""

    def __init__(self, x_posi, y_posi):
        """constructeur de classe"""
        self.position_x = x_posi # position sur la largeur
        self.position_y = y_posi # position sur la hauteur
        self.items_collected = 0 # inventaire des items collectés

        # self.image = MAC_PIC # image associé au personnage
        self.is_alive = True # statut du personnage
        # self.laby = map.Map()

        # self.position = position.Position(map.Map.mcg_spawn[0][0], 0)


    def pick_item(self):
        """Methode qui permet de collecter un objet en passant dessus"""
        # if position player == position item:
            # self.items_collected += 1
        pass


    def move_char(self, x, y):
        """méthode qui permet d'autoriser les déplacements...
         du personnage dans le labyrinthe"""
        self.position_x = x
        self.position_y = y



    def die_char(self):
        """méthode qui agit sur le statut du personnage"""
        # if contact guardian and self.items_collected < 3:
        #     self.is_alive = False
        # else:
        #     self.is_alive = True
        pass


    def move_right(self):
        self.position_x += 1

    def move_left(self):
        self.position_x -= 1

    def move_up(self):
        self.position_y += 1

    def move_down(self):
        self.position_y -= 1



if __name__ == '__main__':


    # c = Player(0, 8)
    c = Player(0, 8)
    print(c.position_x)
    print(c.position_y)
    c.move_right()
    c.move_right()
    c.move_right()
    c.move_down()
    c.move_down()
    c.move_down()
    print(c.position_x)
    print(c.position_y)

