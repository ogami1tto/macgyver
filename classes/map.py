#! /usr/bin/env python3
# coding: utf-8

class Map:
    """classe qui construit la carte du labyrinthe"""
    def __init__(self, map):
        """"constructeur de classe"""
        self.map = map


    def create_map(self):
        """methode permettant de transformer le fichier texte en table"""
