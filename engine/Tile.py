import pygame
from engine.Style import Style


class Tile(pygame.Rect):
    def __init__(self, x1, y1, x2, y2, colour, board):
        super().__init__(x1, y1, x2, y2)
        self.board = board

        if colour == "white":
            self.colour = Style.white
            self.originalColour = Style.white
            self.selectedColour = Style.selectedWhite
        else:
            self.colour = Style.black
            self.originalColour = Style.black
            self.selectedColour = Style.selectedBlack

        self.piece = None

    def setPiece(self, piece):
        self.piece = piece

    def removePiece(self):
        self.piece = None

    def setColour(self, colour):
        if colour == "white":
            self.colour = Style.white
            self.originalColour = Style.white
            self.selectedColour = Style.selectedWhite
        else:
            self.colour = Style.black
            self.originalColour = Style.black
            self.selectedColour = Style.selectedBlack

    def draw(self):
        self.board._drawTile(self)
        if self.piece:
            self.piece.draw()

    def select(self):
        self.colour = self.selectedColour

    def unselect(self):
        self.colour = self.originalColour
