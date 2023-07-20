import pygame
from const import *

class Map:
    def __init__(self, game):
        self.game = game

        self.img = self.game.assets['map']
        self.pos = (0, 0)
    
    def render(self, surf):
        surf.blit(self.img, self.pos)
