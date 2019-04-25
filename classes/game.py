# ! /usr/bin/env python3
# coding: utf-8
"""encodage."""

import pygame
from pygame.locals import *
import map
import config


class Game:
    """classe qui gere la boucle du jeu."""

    def __init__(self):
        """Initialisation du labyrinthe."""
        self.laby = map.Map()
        self.grid = self.laby.map_full
        self.position_x = int(self.laby.macgyver.position_x)
        self.position_y = int(self.laby.macgyver.position_y)
        self.mac_posi = int(
            self.laby.macgyver.position_x) * config.sprite_size, int(
                self.laby.macgyver.position_y) * config.sprite_size
        self.needle_posi = (
            int(self.laby.needle.position_x) * config.sprite_size,
            int(self.laby.needle.position_y) * config.sprite_size)
        self.tube_posi = (int(self.laby.tube.position_x) * config.sprite_size,
                          int(self.laby.tube.position_y) * config.sprite_size)
        self.ether_posi = (
            int(self.laby.ether.position_x) * config.sprite_size,
            int(self.laby.ether.position_y) * config.sprite_size)
        self.murdock_posi = (
            int(self.laby.murdock.position_x) * config.sprite_size,
            int(self.laby.murdock.position_y) * config.sprite_size)
        self.floor = self.laby.free_frame
        self.wall = self.laby.wall
        self.items_collected = self.laby.macgyver.items_collected
        self.game_started = False
        self.game_over = False
        self.lost_game = False
        self.good_game = False
        self.run_pygame()

    def check_item(self):
        """Methode qui permet de collecter un objet en passant dessus."""
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
        pygame.display.flip()

    def pick_item(self, item):
        """Method that adds the picked up item to the inventory."""
        self.item = ['needle', 'tube', 'ether']
        self.items_collected += 1
        print("Vous avez ramassé :", item)

    def check_win(self):
        """Method that checks if player is able to beat the guardian."""
        pygame.init()
        self.game_over = True
        self.game_started = False
        if self.items_collected < 3:
            self.laby.macgyver.is_alive = 0
            print("Le Gardien vous a capturé ! Perdu !")
            self.lost_game = True
        else:
            self.laby.macgyver.is_alive = 1
            self.laby.murdock.is_alive = 0
            print("Vous avez endormi le Gardien ! Gagné !")
            self.good_game = True

    def move(self, direction):
        """Methode qui permet les deplacements du personnage."""
        if direction == "right":
            newpos = [str(int(self.position_x) + 1), str(self.position_y)]
        if direction == "left":
            newpos = [str(int(self.position_x) - 1), str(self.position_y)]
        if direction == "up":
            newpos = [str(self.position_x), str(int(self.position_y) - 1)]
        if direction == "down":
            newpos = [str(self.position_x), str(int(self.position_y) + 1)]

        if self.grid[newpos[0], newpos[1]] != "x":
            self.window.blit(
                pygame.image.load(config.FLOOR).convert_alpha(),
                ((int(self.position_x) * config.sprite_size),
                 (int(self.position_y) * config.sprite_size)))
            self.position_x = newpos[0]
            self.position_y = newpos[1]
            self.check_item()

        if self.grid[newpos[0], newpos[1]] == "g":
            self.check_win()

    def run_pygame(self):
        """Fonction qui gere la boucle du jeu."""
        running = True
        pygame.init()  # Pygame library initialization
        pygame.key.set_repeat(100,
                              100)  # Moving player while long pressing on keys
        pygame.time.Clock().tick(40)  # Refresh rate

        self.window = pygame.display.set_mode((config.window_size,
                                               600))  # Pygame window display
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
        while running:
            self.game_started = True
            pygame.time.Clock().tick(30)

            while self.game_started is True:
                for case in self.floor:
                    self.window.blit(floor_pic,
                                     ((int(case[0]) * config.sprite_size),
                                      (int(case[1]) * config.sprite_size)))
                for case in self.wall:
                    self.window.blit(wall_pic,
                                     ((int(case[0]) * config.sprite_size),
                                      (int(case[1]) * config.sprite_size)))
                if self.laby.murdock.is_alive == 1:
                    self.window.blit(murdock_pic, self.murdock_posi)
                if self.laby.needle.item_is_on is True:
                    self.window.blit(needle_pic, self.needle_posi)
                if self.laby.tube.item_is_on is True:
                    self.window.blit(tube_pic, self.tube_posi)
                if self.laby.ether.item_is_on is True:
                    self.window.blit(ether_pic, self.ether_posi)
                if self.laby.macgyver.is_alive == 1:
                    self.window.blit(
                        mac_pic, (int(self.position_x) * config.sprite_size,
                                  int(self.position_y) * config.sprite_size))

                if self.lost_game is not True:
                    pygame.display.flip()

                for event in pygame.event.get():
                    if (
                        event.type == QUIT or
                        event.type == KEYDOWN and
                        event.key == K_ESCAPE
                    ):
                        running = False
                        self.game_started = False
                        print("QUIT")
                        pygame.quit()
                    elif event.type == KEYDOWN:
                        if event.key == K_RIGHT:
                            self.move("right")
                        if event.key == K_LEFT:
                            self.move("left")
                        if event.key == K_UP:
                            self.move("up")
                        if event.key == K_DOWN:
                            self.move("down")
                        self.window.blit(
                            mac_pic,
                            (int(self.position_x) * config.sprite_size,
                             int(self.position_y) * config.sprite_size))

                        pygame.display.flip()

            while self.game_over:
                self.game_started = False
                if self.good_game is True:
                    self.window.blit(
                        pygame.image.load(config.WIN_PIC).convert(), (0, 0))
                    pygame.display.flip()

                if self.lost_game is True:
                    self.window.blit(
                        pygame.image.load(config.LOSE_PIC).convert(), (0, 0))
                    pygame.display.flip()

                for event in pygame.event.get():
                    if (
                        event.type == QUIT or
                        event.type == KEYDOWN and
                        event.key == K_ESCAPE
                    ):
                        running = False
                        pygame.quit()
                        print("quitter")
                    if event.type == KEYDOWN:
                        if event.key == K_RETURN or event.key == K_SPACE:
                            """The player want to restart the game,
                             so this loop is leaved, game_restart reinit
                             game and the playing game loop come again.
                            """
                            Game()


if __name__ == '__main__':
    new_game = Game()
