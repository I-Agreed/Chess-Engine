import pygame


class Tile(pygame.Rect):
    def __init__(self, x1, y1, x2, y2, colour):
        super().__init__(x1, y1, x2, y2)
        self.colour = colour
        self.piece = None

    def setPiece(self, piece):
        self.piece = piece

    def removePiece(self):
        self.piece = None

    def setColour(self, colour):
        self.colour = colour

    def draw(self):
        self.board._drawTile(self)
        if self.piece:
            self.piece.draw()
