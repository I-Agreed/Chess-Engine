import pygame


class Tile(pygame.Rect):
    def __init__(self, x1, y1, x2, y2, colour):
        super().__init__(x1, y1, x2, y2)
        self.colour = colour
