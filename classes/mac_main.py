# ! /usr/bin/env python3
# coding: utf-8

import pygame
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
        self.mac_posi = int(self.laby.macgyver.position_x) * config.sprite_size, int(self.laby.macgyver.position_y) * config.sprite_size
        self.needle_posi = (int(self.laby.needle.position_x) * config.sprite_size,
                            int(self.laby.needle.position_y) * config.sprite_size)
        self.tube_posi = (int(self.laby.tube.position_x) * config.sprite_size,
                          int(self.laby.tube.position_y) * config.sprite_size)
        self.ether_posi = (int(self.laby.ether.position_x) * config.sprite_size,
                           int(self.laby.ether.position_y) * config.sprite_size)
        self.murdock_posi = (int(self.laby.murdock.position_x) * config.sprite_size,
                             int(self.laby.murdock.position_y) * config.sprite_size)
        self.floor = self.laby.free_frame
        self.wall = self.laby.wall
        self.items_collected = self.laby.macgyver.items_collected  # inventaire des items collectés
        self.game_over = False
        self.good_game = False
        self.run_pygame()

    def check_item(self):
        if [int(self.position_x), int(self.position_y)] == [
            int(self.laby.needle.position_x),
            int(self.laby.needle.position_y)
        ]:
            self.laby.needle.item_is_on = False
            if self.laby.needle.collected is False:
                self.pick_item('needle')
                self.laby.needle.collected = True
                print("Objets ramassés :", self.items_collected)

        if [int(self.position_x), int(self.position_y)] == [
            int(self.laby.tube.position_x),
            int(self.laby.tube.position_y)
        ]:
            self.laby.tube.item_is_on = False
            if self.laby.tube.collected is False:
                self.pick_item('tube')
                self.laby.tube.collected = True
                print("Objets ramassés :", self.items_collected)

        if [int(self.position_x), int(self.position_y)] == [
            int(self.laby.ether.position_x),
            int(self.laby.ether.position_y)
        ]:
            self.laby.ether.item_is_on = False
            if self.laby.ether.collected is False:
                self.pick_item('ether')
                self.laby.ether.collected = True
                print("Items ramassés :", self.items_collected)

    def pick_item(self, item):
        """Methode qui permet de collecter un objet en passant dessus"""
        self.item = ['needle', 'tube', 'ether']
        self.items_collected += 1
        print("Vous avez ramassé :", item)

    def check_win(self):
        """méthode qui verifie si le personnage peut battre le gardien"""
        # quit_game = pygame.display.set_mode((225, 225))

        if self.items_collected < 3:
            self.laby.macgyver.is_alive = 0
            print("Le Gardien vous a capturé ! Perdu !")
            self.game_over = True
            # quit_game.blit(pygame.image.load(constants.win).convert(), (0,0))
        else:
            self.laby.macgyver.is_alive = 1
            self.laby.murdock.is_alive = 0
            print("Vous avez endormi le Gardien ! Gagné !")
            self.good_game = True
            # quit_game.blit(pygame.image.load(constants.loose).convert(), (0,0))

        if self.good_game is True:
            self.window.blit(pygame.image.load(config.BACKGROUND_PIC).convert_alpha(),
                        (0, 30))
            font = pygame.font.Font(None, 25)
            text = font.render("C'est gagné !!! MacGyver s'est évadé !", 1,
                               (255, 255, 255))  # Display the text in white with rounded edge
            textrect = text.get_rect()
            # textrect.centerx, textrect.centery = Window_Size / 2, Window_Size / 2  # Centering the text
            self.window.blit(text, textrect)

            pygame.display.flip()

        if self.game_over is True:
            self.window.blit(pygame.image.load(config.BACK).convert_alpha(),
                        (0, 30))  # draw over everything on the screen now by re-drawing the background
            font = pygame.font.Font(None, 25)
            text = font.render("Perdu... Murdock vous a empêché de vous évader.", 1,
                               (255, 255, 255))  # Display the text in white with rounded edge
            textrect = text.get_rect()
            # textrect.centerx, textrect.centery = window_size / 2, window_size / 2
            self.window.blit(text, textrect)

            pygame.display.flip()

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
            self.window.blit(pygame.image.load(config.FLOOR).convert_alpha(),
                        ((int(self.position_x) * config.sprite_size), (int(self.position_y) * config.sprite_size)))
            self.position_x = newpos[0]
            self.position_y = newpos[1]
            self.check_item()

        if self.grid[newpos[0], newpos[1]] == "g":
            self.check_win()

    def run_pygame(self):
        """Fonction qui gère la boucle du jeu"""

        pygame.init()  # Pygame library initialization
        pygame.font.init()

        self.window = pygame.display.set_mode((config.window_size, 600))  # Pygame window display
        pygame.display.set_caption(config.TITLE)  # Window title
        icon = pygame.image.load(config.ICON).convert_alpha()  # App icon
        pygame.display.set_icon(icon)

        mac_pic = pygame.image.load(config.MAC).convert_alpha()
        murdock_pic = pygame.image.load(config.GUARD).convert_alpha()
        needle_pic = pygame.image.load(config.NEEDLE).convert_alpha()
        tube_pic = pygame.image.load(config.TUBE).convert_alpha()
        ether_pic = pygame.image.load(config.ETHER).convert_alpha()
        wall_pic = pygame.image.load(config.WALL).convert_alpha()
        floor_pic = pygame.image.load(config.FLOOR).convert_alpha()

        pygame.display.flip()

        # Main loop
        game_over = False
        clock = pygame.time.Clock()
        pygame.key.set_repeat(500, 50)  # Moving player while pressing long on key

        for case in self.floor:
            self.window.blit(floor_pic,
                        ((int(case[0]) * config.sprite_size), (int(case[1]) * config.sprite_size)))
        for case in self.wall:
            self.window.blit(wall_pic,
                        ((int(case[0]) * config.sprite_size), (int(case[1]) * config.sprite_size)))
        if self.laby.murdock.is_alive is True:
            self.window.blit(murdock_pic, self.murdock_posi)
        if self.laby.needle.item_is_on is True:
            self.window.blit(needle_pic, (self.needle_posi))
        if self.laby.tube.item_is_on is True:
            self.window.blit(tube_pic, (self.tube_posi))
        if self.laby.ether.item_is_on is True:
            self.window.blit(ether_pic, (self.ether_posi))

        while not game_over:
            pygame.time.Clock().tick(40)  # Refresh rate# Loop speed limit to not overload the processor (30 frames per second)
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    game_over = True
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.move("right")
                    if event.key == K_LEFT:
                        self.move("left")
                    if event.key == K_UP:
                        self.move("up")
                    if event.key == K_DOWN:
                        self.move("down")

                    self.window.blit(mac_pic, (int(self.position_x) * config.sprite_size, int(self.position_y) * config.sprite_size))

            # window.blit(pygame.image.load(config.EXIT).convert_alpha(),
            #             ((int(case[0]) * config.sprite_size), (int(case[1]) * config.sprite_size)))

            clock.tick(60)
            pygame.display.flip()

        # image background loading
        # background = pygame.image.load(config.BACKGROUND_PIC).convert()
        # background = pygame.transform.scale(background, (config.window_size, 600))
        # window.blit(background, (0, 0))

if __name__ == '__main__':

    new_game = Game()