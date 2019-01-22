#! /usr/bin/env python3
# coding: utf-8

# import pygame
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
        # self.game_on = True


    def check_item(self):
        if [int(self.position_x), int(self.position_y)] == [int(self.laby.aiguille.position_x), int(self.laby.aiguille.position_y)]:
            self.pick_item()
        if [int(self.position_x), int(self.position_y)] == [int(self.laby.tube.position_x), int(self.laby.tube.position_y)]:
            self.pick_item()
        if [int(self.position_x), int(self.position_y)] == [int(self.laby.ether.position_x), int(self.laby.ether.position_y)]:
            self.pick_item()


    def pick_item(self):
        """Methode qui permet de collecter un objet en passant dessus"""
        self.items_collected += 1
        print("Vous avez ramassé l'objet.")
        # Faire disparaître les items une fois collectés par le personnage !!!
        self.laby.ether.item_is_on = False


    def move(self, direction):
        """méthode qui permet les deplacements du personnage"""
        if direction == "right":
                newpos = [str(int(self.position_x)+1), str(self.position_y)]
        if direction == "left":
                newpos = [str(int(self.position_x)-1), str(self.position_y)]
        if direction == "up":
                newpos = [str(self.position_x), str(int(self.position_y)-1)]
        if direction == "down":
                newpos = [str(self.position_x), str(int(self.position_y)+1)]

        if self.grid[newpos[0], newpos[1]] != "x":
            self.position_x = newpos[0]
            self.position_y = newpos[1]
            self.check_item()


    def check_win(self):
        """méthode qui verifie si le personnage peut battre le gardien"""
        if self.grid[str(self.position_x), str(self.position_y)] == position_guardian:
            if self.items_collected < 3:
                self.laby.macgyver.is_alive = False
                print("Le Gardien vous a capturé ! Perdu !")
        else:
            self.laby.macgyver.is_alive = True
            self.laby.murdock.is_alive = False
            print("Vous avez endormi le Gardien ! Gagné !")


    def game_over(self):
        if self.laby.macgyver.is_alive == False:
            pass


if __name__ == '__main__':
    m = Game()
