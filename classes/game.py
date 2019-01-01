#! /usr/bin/env python3
# coding: utf-8

import map
import config
import player
import guardian
import item

class Game:
    """classe qui gère la boucle du jeu"""
    def __init__(self):
        self.laby = map.Map()
        self.grid = self.laby.map_full
        self.position_x = int(self.laby.macgyver.position_x)
        self.position_y = int(self.laby.macgyver.position_y)
        self.items_collected = 0 # inventaire des items collectés
        self.ether = self.laby.ether
        # self.game_on = True


    def check_item(self):
        if [self.position_x, self.position_y] == [self.laby.ether.position_x, self.laby.ether.position_y]:
            self.pick_item()


    def pick_item(self):
        """Methode qui permet de collecter un objet en passant dessus"""
        self.items_collected += 1
        # Faire disparaître les items une fois collectés par le personnage !!!
        self.laby.ether.item_is_on = False


    def move(self, direction):
        """méthode qui permet les deplacements du personnage"""
        if direction == "right":
            if self.grid[str(self.position_x+1), str(self.position_y)] != "x":
                self.position_x+=1
                self.check_item()
        if direction == "left":
            if self.grid[str(self.position_x-1), str(self.position_y)] != "x":
                 self.position_x-=1
                 self.check_item()
        if direction == "up":
            if self.grid[str(self.position_x), str(self.position_y-1)] != "x":
                 self.position_y-=1
                 self.check_item()
        if direction == "down":
            if self.grid[str(self.position_x), str(self.position_y+1)] != "x":
                self.position_y+=1
                self.check_item()


    # def check_win(self):
    #     """méthode qui agit sur le statut du personnage"""
    #     # if position_player == position_guardian and self.items_collected < 3:
    #     #     self.is_alive = False
    #     # else:
    #     #     self.is_alive = True
    #     pass


if __name__ == '__main__':
    m = Game()
    # print(m.laby.macgyver.position_x)
    # print("Coordonnees items :", m.laby.items)
    # print("MacGyver spawn :", m.laby.mcg_spawn)
    # print("MacGyver position depuis module Map :")
    # print(m.laby.macgyver.position_x, m.laby.macgyver.position_y)
    # print("------")
    # print(m.grid[str(m.position_x), str(m.position_y)])
    m.move("up")
    m.move("right")
    m.move("right")
    m.move("right")
    m.move("down")
    # print("------")
    print("MacGyver position depuis module Map :")
    print(m.laby.macgyver.position_x, m.laby.macgyver.position_y)
    print("MacGyver position depuis module Game :")
    print(m.position_x, m.position_y)
    print("Valeur du dico 'full_map' aux memes coordonnees :")
    print(m.grid[str(m.position_x), str(m.position_y)])
    # print("------")
    # print("MacGyver position depuis module Map :")
    # print(m.laby.macgyver.position_x, m.laby.macgyver.position_y)
    # print(m.valeur)
    print("Ether position depuis module Map :")
    print(m.laby.ether.position_x, m.laby.ether.position_y)
    print(m.laby.ether.item_is_on)
    print((m.laby.ether.position_x, m.laby.ether.position_y), (m.position_x, m.position_y))
    print(m.items_collected)
    print(m.laby.ether.position_x)
    print(m.laby.ether.item_is_on)
    # print(m.position_y)
    # print(int(m.laby.macgyver.position_y))


