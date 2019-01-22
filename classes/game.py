#! /usr/bin/env python3
# coding: utf-8

import pygame
from pygame.locals import *
import map
import config


class Game:
    """classe qui gère la boucle du jeu"""

    def __init__(self):
        self.laby = map.Map()
        self.grid = self.laby.map_full
        self.position_x = int(self.laby.macgyver.position_x)
        self.position_y = int(self.laby.macgyver.position_y)
        self.items_collected = 0  # inventaire des items collectés
        self.needle_posi = (int(self.laby.needle.position_x), int(self.laby.macgyver.position_y))
        self.check_win()
        self.pygame()


    def check_item(self):
        if [int(self.position_x), int(self.position_y)] == [
                int(self.laby.needle.position_x),
                int(self.laby.needle.position_y)
        ]:
            self.pick_item()
        if [int(self.position_x), int(self.position_y)] == [
                int(self.laby.tube.position_x),
                int(self.laby.tube.position_y)
        ]:
            self.pick_item()
        if [int(self.position_x), int(self.position_y)] == [
                int(self.laby.ether.position_x),
                int(self.laby.ether.position_y)
        ]:
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

    def check_win(self):
        """méthode qui verifie si le personnage peut battre le gardien"""
        # quit_game = pygame.display.set_mode((225, 225))
        if self.grid[str(self.position_x
                         ), str(self.position_y)] == [
                             self.laby.guardian_spawn[0][0],
                             self.laby.guardian_spawn[0][1]
                         ]:
            if self.items_collected < 3:
                self.laby.macgyver.is_alive = False
                print("Le Gardien vous a capturé ! Perdu !")
                proceed = 0
                # quit_game.blit(pygame.image.load(constants.win).convert(), (0,0))
        else:
            self.laby.macgyver.is_alive = True
            self.laby.murdock.is_alive = False
            print("Vous avez endormi le Gardien ! Gagné !")
            proceed = 0
            # quit_game.blit(pygame.image.load(constants.loose).convert(), (0,0))

        # pygame.display.flip() #Refresh the window

    def pygame(self):
        """methode qui contient la boucle du jeu et la gestion de
        l'affichage par le biais de la bibliothèthe Pygame"""

        pygame.init()  # Pygame library initialization
        # pygame.font.init()
        window = pygame.display.set_mode((config.window_size, 600))  # Pygame window display
        pygame.display.set_caption(config.TITLE)  # Title
        icon = pygame.image.load(config.ICON).convert_alpha()  # Icone
        pygame.display.set_icon(icon)
        clock = pygame.time.Clock()  # Refresh rate

        # image background loading
        background = pygame.image.load(config.BACKGROUND_PIC).convert()
        background = pygame.transform.scale(background, (config.window_size, 600))
        window.blit(background, (0, 0))

        # # display macgyver and set position and resize icon
        mac_image = pygame.image.load(config.MAC_PIC).convert_alpha()
        # macgyver_icon = pygame.transform.scale(macgyver_icon, (30, 35))
        mac_posi = (self.position_x, self.position_y)


        # display pictures of all objects
        wall_image = pygame.image.load(config.WALL_PIC).convert()
        floor_image = pygame.image.load(config.FLOOR_PIC).convert()
        # displaying the objects png's
        tube_image = pygame.image.load(config.TUBE).convert_alpha()
        # window.blit(tube_image, (0, 50))
        needle_image = pygame.image.load(config.NEEDLE).convert_alpha()
        ether_image = pygame.image.load(config.ETHER).convert_alpha()


        # Main loop
        # create an instance for the maze
        new_game = Game()
        run = True
        while run:
            # Loop speed limit to not overload the processor (30 frames per second)
            pygame.time.delay(100)
            # pygame.time.Clock().tick(40)  #Loop speed limit to not overload the processor (30 frames per second)

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

        # Re-pasting after the events
        window.blit(background, (0, 30))  # the background is streched from below the black margin to the opposite corner
        # map.display(Window)
        window.blit(mac_image, mac_posi)

        pygame.quit()



if __name__ == '__main__':
    m = Game()
    # m.move("up")
    # m.move("right")
    # m.move("right")
    # m.move("right")
    # m.move("down")
    # print("------")
    # print("MacGyver position depuis module Map :")
    # print(m.laby.macgyver.position_x, m.laby.macgyver.position_y)
    # print("MacGyver position depuis module Game :")
    # print(m.position_x, m.position_y)
    # print("Valeur du dico 'full_map' aux memes coordonnees :")
    # print(m.grid[str(m.position_x), str(m.position_y)])
    # print("------")
    # print("MacGyver position depuis module Map :")
    # print(m.laby.macgyver.position_x, m.laby.macgyver.position_y)
    # print(m.valeur)
    # print("Items position depuis module Map :")
    # print(m.laby.items)
    # print(m.laby.ether.item_is_on)
    # print(newpos[0], newpos[1])
    # print((m.position_x, m.position_y))
    # print(m.items_collected)
    # print(m.laby.ether.item_is_on)
    # print("--------------------")



    # display message at the end of the game
    # myfont1 = pygame.font.SysFont("monospace", 34)
    # win = myfont1.render('Gagné !', False, (255, 255, 0))
    # lost = myfont1.render('Perdu !', False, (255, 255, 0))

    # display the counter
    # myfont = pygame.font.SysFont("monospace", 26)

    # set the item counter to 0
    # self.nb_item = 0
    # self.counter_display = self.myfont.render("x " + str(self.nb_item), False, (255,255,0))
    # self.item_counter = pygame.image.load("images/potion.png").convert()

    # refresh the screen and display the background and player
    # pygame.display.flip()

        # Show the labyrinth on the window
        # window.fill((0, 0, 0))  #Reset the screen for the inventory
        # maze.show(window)
        # wall_image = pygame.image.load(constants.wall).convert()
        # floor_image = pygame.image.load(constants.floor).convert()
        # for o, row in enumerate(self.LAB_STRUCTURE):
        #     for h, column in enumerate(row):
        #         position = Position(o,h)
        #         if self.LAB_STRUCTURE[o][h] == constants.wall_symbol:
        #             window.blit(wall_image,(position.x, position.y))
        #         else:
        #             self.LAB_STRUCTURE[o][h] == constants.floor_symbol
        #             window.blit(floor_image,(position.x, position.y))

        # for element in labyrinth_elements:
        #     window.blit(element.image,
        #                 (element.position.x, element.position.y))

        # pygame.display.flip()


    # start_tick = pygame.time.get_ticks(
    # )  #Get a number of frames to display the win or loose image window
    # while stop:
    #     time = (pygame.time.get_ticks() - start_tick) / 1000
    #     pygame.init()
    #     quit_game = pygame.display.set_mode((225, 225))
    #     if characters.objects_num == 3:
    #         quit_game.blit(pygame.image.load(constants.win).convert(), (0,0))
    #     else:
    #         quit_game.blit(pygame.image.load(constants.loose).convert(), (0,0))

    #     pygame.display.flip() #Refresh the window
    #     classes.Endgame.win(macgyver, maze)
        #After 5 seconds close all the windows
        # if time > 2:
        #     stop = 0







    # pygame.init()  # Pygame library initialization
    # # pygame.font.init()
    # window = pygame.display.set_mode((config.window_size, 600))  # Pygame window display
    # pygame.display.set_caption(config.TITLE)  # Title
    # icon = pygame.image.load(config.ICON).convert_alpha()  # Icone
    # pygame.display.set_icon(icon)

    # clock = pygame.time.Clock()  # Refresh rate

    # new_game = Game()  # create an instance for the maze

    # # image background loading
    # background = pygame.image.load(config.BACKGROUND_PIC).convert()
    # background = pygame.transform.scale(background, (config.window_size, 600))
    # window.blit(background, (0, 0))

    # # # display macgyver and set position and resize icon
    # mac_image = pygame.image.load(config.MAC_PIC).convert_alpha()
    # mac_posi = (new_game.position_x, new_game.position_y)

    # # # macgyver_icon = pygame.transform.scale(macgyver_icon, (30, 35))

    # # # display pictures of all objects
    # # wallIMG = pygame.image.load(config.WALL_PIC).convert()
    # # floorIMG = pygame.image.load(config.FLOOR_PIC).convert()

    # # displaying the objects png's
    # tube_image = pygame.image.load(config.TUBE).convert_alpha()
    # # window.blit(tube_image, (0, 50))
    # needle_image = pygame.image.load(config.NEEDLE).convert_alpha()
    # ether_image = pygame.image.load(config.ETHER).convert_alpha()

    # # # refreshing the screen for the background to be visible over the default one
    # # pygame.display.flip()

    # # Main loop
    # # new_game = Game()  # create an instance for the maze
    # run = True

    # # pygame.key.set_repeat(400, 30)  #Moving MaGyver by maintening a arrow_key pressed

    # # new_game.display(window)
    # # tube.display(tubeIMG, window)
    # # needle.display(needleIMG, window)
    # # ether.display(etherIMG, window)


    # while run:
    #     # Loop speed limit to not overload the processor (30 frames per second)
    #     pygame.time.delay(100)
    #     # pygame.time.Clock().tick(40)  #Loop speed limit to not overload the processor (30 frames per second)
    #     for event in pygame.event.get():
    #         if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
    #             run = False
    #         if event.type == KEYDOWN:
    #             if event.key == K_RIGHT:
    #                 new_game.move("right")
    #             if event.key == K_LEFT:
    #                 new_game.move("left")
    #             if event.key == K_UP:
    #                 new_game.move("up")
    #             if event.key == K_DOWN:
    #                 new_game.move("down")
    #     window.blit(mac_image, mac_posi)
    #     pygame.display.flip()

    # pygame.quit()