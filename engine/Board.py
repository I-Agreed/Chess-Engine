import pygame
from engine.Tile import Tile


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
                                           [(255, 255, 255), (0, 0, 0)][(i + j) % 2]))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def _drawTile(self, tile):
        pygame.draw.rect(self.screen, tile.colour, tile)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for i in self.tiles:
            for j in i:
                self._drawTile(j)
        pygame.display.flip()

    def mainloop(self):
        while 1:
            self.events()
            self.draw()

    def thread(self):
        pass

if __name__ == "__main__":
    board = Board()
    board.mainloop()
