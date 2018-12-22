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
        # self.joueur = player.Player(self.laby.mcg_spawn[0][0], self.laby.mcg_spawn[0][1])
        self.position_x = int(self.laby.mcg_spawn[0][0])
        self.position_y = int(self.laby.mcg_spawn[0][1])
        # self.macgyver = player.Player(self.mcg_spawn[0][0], self.mcg_spawn[0][1])


    def move_right(self):
        if "x" == m.grid[str(m.position_x+1), str(m.position_y)]:
            self.position_x += 0
        else:
            self.position_x += 1

    def move_left(self):
        if "x" == m.grid[str(m.position_x-1), str(m.position_y-1)]:
            self.position_x += 0
        else:
            self.position_x -= 1

    def move_up(self):
        # if str(m.grid[int(m.position_x), int(m.position_y)]) == "x":
        if "x" == m.grid[str(m.position_x), str(m.position_y-1)]:
            self.position_y += 0
        else:
            self.position_y -= 1

    def move_down(self):
        if "x" == m.grid[str(m.position_x), str(m.position_y+1)]:
            self.position_y += 0
        else:
            self.position_y += 1

    # def check_next_move(self):
    #     """methode qui verifie si le personnage peut aller dans...
    #      la direction donnee"""
    #     if m.grid[str(m.position_x), str(m.position_y)] != "x":


if __name__ == '__main__':
    m = Game()
    print(m.laby.items)
    print(m.laby.mcg_spawn)
    print(m.laby.mcg_spawn[0][0], m.laby.mcg_spawn[0][1])
    print("BREAK")
    # print(m.player.position_y)
    print(m.grid[str(m.position_x), str(m.position_y)])
    m.move_up()
    m.move_right()
    m.move_right()
    m.move_right()
    m.move_down()

    print(m.position_x, m.position_y)
    print(m.grid[str(m.position_x), str(m.position_y)])
    print(m.laby.item_1.position_x, m.laby.item_1.position_y)

    # print(m.grid[str(m.position_x), str(m.position_y)])

    # m.check_next_move()
    # # print(c.position_x)
    # # print(c.position_y)

    # print(m.joueur.position_x, m.joueur.position_y)
