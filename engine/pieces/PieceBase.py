class PieceBase():
    def __init__(self):
        self.x = None
        self.y = None
        self.board = None
        self.tile = None
        self.image = "test"

    def _place(self, x, y, board, tile):
        self.x = x
        self.y = y
        self.board = board
        self.tile = tile

    def _move(self, x, y, tile):
        self.x = x
        self.y = y
        self.tile = tile

    def draw(self):
        self.board.screen.blit(self.board.images["test"], self.tile)

    def getMoves(self):
        return [(i,j) for j in range(self.board.height) for i in range(self.board.width)]