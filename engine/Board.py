import pygame

class Board:
    def __init__(self, width=8, height=8, tileSize=10):
        pygame.init()
        self.tileSize = tileSize
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((tileSize*width, tileSize*height))

        self.tiles = []
        for i in range(self.width):
            self.tiles.append([])
            for j in range(self.height):
                self.tiles[-1].append(pygame.Rect(i*self.tileSize, j*self.tileSize,
                                                 i*(self.tileSize + 1), j*(self.tileSize + 1)))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def mainloop(self):
        while 1:
            self.events()
            self.draw()

if __name__ == "__main__":
    board = Board()
    board.mainloop()
