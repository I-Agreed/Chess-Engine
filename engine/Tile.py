import pygame
from engine.Style import Style


class Tile(pygame.Rect):
    def __init__(self, x1, y1, x2, y2, colour, board, tileX, tileY):
        super().__init__(x1, y1, x2, y2)
        self.board = board

        self.tileX = tileX
        self.tileY = tileY
        self.pos = tileX, tileY

        if colour == "white":
            self.colour = Style.white
            self.originalColour = Style.white
            self.selectedColour = Style.selectedWhite
            self.highlightedColour = Style.highlightedWhite
        else:
            self.colour = Style.black
            self.originalColour = Style.black
            self.selectedColour = Style.selectedBlack
            self.highlightedColour = Style.highlightedBlack

        self.piece = None

        self.isHighlighted = False
        self.isSelected = False

    def setPiece(self, piece):
        self.piece = piece

    def removePiece(self):
        self.piece = None

    def setColour(self, colour):
        if colour == "white":
            self.colour = Style.white
            self.originalColour = Style.white
            self.selectedColour = Style.selectedWhite
            self.highlightedColour = Style.highlightedWhite
        else:
            self.colour = Style.black
            self.originalColour = Style.black
            self.selectedColour = Style.selectedBlack
            self.highlightedColour = Style.highlightedBlack

    def draw(self):
        self.board._drawTile(self)
        if self.piece:
            self.piece.draw()

    def select(self):
        self.colour = self.selectedColour
        self.isSelected = True

    def unselect(self):
        self.colour = self.originalColour
        self.isSelected = False

    def highlight(self):
        self.colour = self.highlightedColour
        self.isHighlighted = True

    def unhighlight(self):
        self.colour = self.originalColour
        self.isHighlighted = False
