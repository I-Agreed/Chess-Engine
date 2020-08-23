import pygame
from engine.Tile import Tile
from engine.images import getImages
from engine.pieces import *
from engine.Style import Style
from engine.Layout import Layout

import ctypes


class Board:
    def __init__(self, width=8, height=8, tileSize=50, padding=5, border=5, blackControl="human", whiteControl="human"):

        self.border = border
        self.padding = padding
        pygame.init()
        self.tileSize = tileSize
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((tileSize * width + (self.padding + self.border) * 2,
                                               tileSize * height + (self.padding + self.border) * 2))
        self.pieces = []
        self.tiles = []
        for i in range(self.width):
            self.tiles.append([])
            for j in range(self.height):
                self.tiles[-1].append(Tile((self.padding + self.border) + i * self.tileSize,
                                           (self.padding + self.border) + j * self.tileSize,
                                           self.tileSize, self.tileSize,
                                           ["white", "black"][(i + j) % 2], self, i, j))

        self.images = getImages(self.tileSize)
        self.turnColour = "white"
        pygame.display.set_caption(f"{self.turnColour} Turn")
        self.selectedTile = None
        self.highlightedTiles = []

        self.control = {}
        self.control["black"] = blackControl
        self.control["white"] = whiteControl
        self.kings = {}

    def setPlayers(self, white="human", black="human"):
        self.control["white"] = white
        self.control["black"] = black

        if self.control[self.turnColour] != "human":
            self.control[self.turnColour].eval_turn()
            self.swapTurns()

    def getKing(self, colour):
        if colour in self.kings:
            return self.kings[colour]
        else:
            for i in self.pieces:
                if isinstance(i, King.King) and i.colour == colour:
                    self.kings[colour] = i
                    return i
        return None

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
            self.unselect()
        elif self.selectedTile is not None:
            if self.tiles[tileX][tileY].isHighlighted:
                self.movePiece(*self.selectedTile.pos, tileX, tileY)
                self.unselect()
                self.swapTurns()

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
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(True)
        except:
            pass
        while 1:
            self.events()
            self.draw()

    def place(self, x, y, piece):
        self.tiles[x][y].setPiece(piece)
        self.pieces.append(piece)
        piece._place(x, y, self, self.tiles[x][y])

    def movePiece(self, x, y, dx, dy):
        self.tiles[dx][dy].piece = self.tiles[x][y].piece
        self.tiles[x][y].piece = None
        self.tiles[dx][dy].piece._move(dx, dy, self.tiles[dx][dy])

    def getPieces(self, colour=None):
        if colour is not None:
            return list(filter(lambda a: a.colour == colour, self.pieces))
        else:
            return self.pieces

    def thread(self):
        pass

    def isPiece(self, x, y):
        return self.tiles[x][y].piece is not None

    def getPiece(self, x, y):
        return self.tiles[x][y].piece

    def pieceColour(self, x, y):
        if self.isPiece(x, y):
            return self.tiles[x][y].piece.colour
        return False

    def select(self, x, y):
        self.selectedTile = self.tiles[x][y]
        self.selectedTile.select()
        if self.selectedTile.piece is not None:
            for i in self.selectedTile.piece.getMoves():
                self.highlight(*i)

    def unselect(self):
        self.selectedTile.unselect()
        self.selectedTile = None
        self.unhighlightAll()

    def highlight(self, x, y):
        self.tiles[x][y].highlight()
        self.highlightedTiles.append(self.tiles[x][y])

    def unhighlight(self, x, y):
        self.tiles[x][y].unhighlight()
        self.highlightedTiles.remove(self.tiles[x][y])

    def unhighlightAll(self):
        for i in self.highlightedTiles:
            i.unhighlight()
        self.highlightedTiles.clear()

    def end(self, Type="checkmate"):
        print("end")
        self.turnColour = "none"
        pygame.display.set_caption(f"Game over: {Type}")

    def swapTurns(self):
        self.turnColour = ["white", "black"][self.turnColour == "white"]
        pygame.display.set_caption(f"{self.turnColour} Turn")
        gameState = self.checkGameState()
        if gameState != "normal":
            self.end(gameState)

        if self.control[self.turnColour] != "human":
            self.control[self.turnColour].eval_turn()
            self.swapTurns()

    def setup(self, layout, white="human", black="human"):
        self.setPlayers(white, black)
        pieces = {"p": Pawn.Pawn,
                  "r": Rook.Rook,
                  "n": Knight.Knight,
                  "k": King.King,
                  "q": Queen.Queen,
                  "b": Bishop.Bishop}
        layout = Layout().__getattribute__(layout).split("\n")
        for y, i in enumerate(layout):
            for x, j in enumerate(i):
                if j != ".":
                    colour = ["black", "white"][j.isupper()]
                    self.place(x, y, pieces[j.lower()](colour))

    def checkGameState(self):
        stalemate = True
        checkmate = False
        for i in self.getPieces(self.turnColour):
            moves = i.getMoves()
            if len(moves) > 0:
                stalemate = False
                break
        if self.getKing(self.turnColour).isInCheck():
            checkmate = True
        return ("normal", "checkmate", "stalemate")[checkmate + stalemate * 2]


if __name__ == "__main__":
    board = Board()
    board.setup("standard")
    board.mainloop()
