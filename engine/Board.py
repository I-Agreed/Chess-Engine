import pygame
from engine.Tile import Tile
from engine.images import getImages
from engine.pieces import *
from engine.Style import Style


class Board:
    def __init__(self, width=8, height=8, tileSize=50, padding=5, border=5):
        self.border = border
        self.padding = padding
        pygame.init()
        self.tileSize = tileSize
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((tileSize * width + (self.padding + self.border) * 2,
                                               tileSize * height + (self.padding + self.border) * 2))

        self.tiles = []
        for i in range(self.width):
            self.tiles.append([])
            for j in range(self.height):
                self.tiles[-1].append(Tile((self.padding + self.border) + i * self.tileSize,
                                           (self.padding + self.border) + j * self.tileSize,
                                           self.tileSize, self.tileSize,
                                           ["white", "black"][(i + j) % 2], self))

        self.images = getImages(self.tileSize)
        self.turnColour = "white"
        self.selectedTile = None

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONUP:

                pos = pygame.mouse.get_pos()
                self.mouseEvent((pos[0] - self.padding - self.border) // self.tileSize,
                                (pos[1] - self.padding - self.border) // self.tileSize)

    def mouseEvent(self, tileX, tileY):
        if tileX < 0 or tileX >= self.width or \
                tileY < 0 or tileY >= self.height:
            return
        if self.selectedTile is self.tiles[tileX][tileY]:
            self.deselect()
        else:
            if self.tiles[tileX][tileY].piece is not None and \
                    self.tiles[tileX][tileY].piece.colour == self.turnColour:
                self.select(tileX, tileY)


    def _drawTile(self, tile):
        pygame.draw.rect(self.screen, tile.colour, tile)

    def draw(self):
        self.screen.fill(Style.background)
        for i in self.tiles:
            for j in i:
                j.draw()
        pygame.display.flip()

    def mainloop(self):
        while 1:
            self.events()
            self.draw()

    def place(self, x, y, piece):
        self.tiles[x][y].setPiece(piece)
        piece._place(x, y, self, self.tiles[x][y])

    def thread(self):
        pass

    def isPiece(self, x, y):
        return self.tiles[x][y].piece is not None

    def select(self, x, y):
        self.selectedTile = self.tiles[x][y]
        self.selectedTile.select()

    def deselect(self):
        self.selectedTile.unselect()
        self.selectedTile = None


if __name__ == "__main__":
    board = Board()
    piece = PieceBase.PieceBase("white")
    board.place(0, 0, piece)
    piece2 = PieceBase.PieceBase("black")
    board.place(1, 0, piece2)
    board.mainloop()
