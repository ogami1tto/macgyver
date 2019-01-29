#! /usr/bin/env python3
# coding: utf-8

import pygame
import os
from pygame.locals import *
import map
import config


class Game:
    """classe qui gère la boucle du jeu"""

    def __init__(self):
        self.laby = map.Map()  # Initialisation du labyrinthe
        self.grid = self.laby.map_full
        self.position_x = int(self.laby.macgyver.position_x)
        self.position_y = int(self.laby.macgyver.position_y)
        # self.mac_posi = [(int(self.laby.macgyver.position_x) * config.sprite_size), (int(self.laby.macgyver.position_y) * config.sprite_size)]
        self.mac_posi = ((int(self.laby.macgyver.position_x) * config.sprite_size), (int(self.laby.macgyver.position_y) * config.sprite_size))
        self.needle_posi = (int(self.laby.needle.position_x) * config.sprite_size, int(self.laby.needle.position_y) * config.sprite_size)
        self.tube_posi = (int(self.laby.tube.position_x) * config.sprite_size, int(self.laby.tube.position_y) * config.sprite_size)
        self.ether_posi = (int(self.laby.ether.position_x) * config.sprite_size, int(self.laby.ether.position_y) * config.sprite_size)
        self.murdock_posi = (int(self.laby.murdock.position_x) * config.sprite_size, int(self.laby.murdock.position_y) * config.sprite_size)
        self.floor = self.laby.free_frame
        self.wall = self.laby.wall
        self.items_collected = 0  # inventaire des items collectés
        self.run_pygame()


    def check_item(self):
        if [int(self.position_x), int(self.position_y)] == [
                int(self.laby.needle.position_x),
                int(self.laby.needle.position_y)
        ]:
            self.laby.needle.item_is_on = 0
            self.pick_item('needle')
        if [int(self.position_x), int(self.position_y)] == [
                int(self.laby.tube.position_x),
                int(self.laby.tube.position_y)
        ]:
            self.laby.tube.item_is_on = 0
            self.pick_item('tube')
        if [int(self.position_x), int(self.position_y)] == [
                int(self.laby.ether.position_x),
                int(self.laby.ether.position_y)
        ]:
            self.laby.ether.item_is_on = 0
            self.pick_item('ether')


    def pick_item(self, item):
        """Methode qui permet de collecter un objet en passant dessus"""
        self.item = ['needle', 'tube', 'ether']
        self.items_collected += 1
        # self.laby.ether.item_is_on = False
        print("Vous avez ramassé :", item )
        # Faire disparaître les items une fois collectés par le personnage !!!


    def move(self, direction):
        """méthode qui permet les deplacements du personnage"""
        if direction == "right":
            newpos = [str(int(self.position_x) + 1), str(self.position_y)]
        if direction == "left":
            newpos = [str(int(self.position_x) - 1), str(self.position_y)]
        if direction == "up":
            newpos = [str(self.position_x), str(int(self.position_y) - 1)]
        if direction == "down":
            newpos = [str(self.position_x), str(int(self.position_y) + 1)]

        if self.grid[newpos[0], newpos[1]] != "x":
            self.position_x = newpos[0]
            self.position_y = newpos[1]
            self.check_item()
            if self.grid[str(self.position_x), str(self.position_y)] == [
                self.laby.guardian_spawn[0][0],
                self.laby.guardian_spawn[0][1]]:
                self.check_win()


    def check_win(self):
        """méthode qui verifie si le personnage peut battre le gardien"""
        # quit_game = pygame.display.set_mode((225, 225))

        if self.items_collected < 3:
                self.laby.macgyver.is_alive = 0
                print("Le Gardien vous a capturé ! Perdu !")
                run = 0
                # quit_game.blit(pygame.image.load(constants.win).convert(), (0,0))
        else:
            self.laby.macgyver.is_alive = 1
            self.laby.murdock.is_alive = 0
            print("Vous avez endormi le Gardien ! Gagné !")
            run = 0
            # quit_game.blit(pygame.image.load(constants.loose).convert(), (0,0))


    # def on_screen(self,image,position):
        # self.image = image
        # self.position = position
        # calcul_affichage = ((position_x * config.sprite_size), (position_y * config.sprite_size))
        # self.screen.blit(self.macgyver.image, (self.macgyver_pos[0] * config.sprite_size, self.macgyver_pos[1] * config.sprite_size))
        # window.blit(image, ((position[0] * config.sprite_size), (position[1] * config.sprite_size)))
        # window.blit(image, (position[0], position[1]))
        # print("image", ((position[0] * config.sprite_size), (position[1] * config.sprite_size)))


    def run_pygame(self):
        """Fonction qui gère la boucle du jeu"""

        pygame.init()  # Pygame library initialization
        # pygame.font.init()

        window = pygame.display.set_mode((config.window_size, 600))  # Pygame window display
        pygame.display.set_caption(config.TITLE)  # Window title
        icon = pygame.image.load(config.ICON).convert_alpha()  # App icon
        pygame.display.set_icon(icon)
        mac_pic = pygame.image.load(config.MAC_PIC).convert_alpha()

        pygame.display.flip()

        # Main loop
        run = True
        clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 50)  #Moving MaGyver by maintening a arrow_key pressed

        while run:
            # pygame.time.Clock().tick(40)  # Refresh rate# Loop speed limit to not overload the processor (30 frames per second)
            # pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    run = False
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.move("right")
                    if event.key == K_LEFT:
                        self.move("left")
                    if event.key == K_UP:
                        self.move("up")
                    if event.key == K_DOWN:
                        self.move("down")
                    print((self.position_x, self.position_y))
                    print((self.mac_posi))

            for case in self.floor:
                window.blit(pygame.image.load(config.FLOOR_PIC).convert_alpha(),
                        ((int(case[0]) * config.sprite_size), (int(case[1]) * config.sprite_size)))

            for case in self.wall:
                window.blit(pygame.image.load(config.WALL_PIC).convert_alpha(),
                        ((int(case[0]) * config.sprite_size), (int(case[1]) * config.sprite_size)))

            window.blit(pygame.image.load(config.EXIT).convert_alpha(),
                        ((int(case[0]) * config.sprite_size), (int(case[1]) * config.sprite_size)))

            window.blit(mac_pic, (self.mac_posi))
            if self.laby.murdock.is_alive == 1:
                window.blit(pygame.image.load(config.MURD_PIC).convert_alpha(), (self.murdock_posi))

            if self.laby.needle.item_is_on == 1:
                window.blit(pygame.image.load(config.NEEDLE).convert_alpha(), (self.needle_posi))
            if self.laby.tube.item_is_on == 1:
                window.blit(pygame.image.load(config.TUBE).convert_alpha(), (self.tube_posi))
            if self.laby.ether.item_is_on == 1:
                window.blit(pygame.image.load(config.ETHER).convert_alpha(), (self.ether_posi))

            clock.tick(60)
            pygame.display.flip()


        # image background loading
        background = pygame.image.load(config.BACKGROUND_PIC).convert()
        background = pygame.transform.scale(background, (config.window_size, 600))
        window.blit(background, (0, 0))

        # # display pictures of all items
        # wall_image = pygame.image.load(config.WALL_PIC).convert_alpha()
        # wall_posi = new_game.laby.wall
        # on_screen(wall_image, (wall_posi)

        # floor_image = pygame.image.load(config.FLOOR_PIC).convert_alpha()
        # floor_posi = new_game.laby.free_frame
        # on_screen(floor_image, (floor_posi))

        # pygame.quit()


if __name__ == '__main__':

    new_game = Game()  # create an instance for the maze


