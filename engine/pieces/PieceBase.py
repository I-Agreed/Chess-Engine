class PieceBase():
    def __init__(self, colour):
        self.x = None
        self.y = None
        self.board = None
        self.tile = None
        self.image = "test_" + colour
        self.colour = colour
        self.hasMoved = False
        self.moves = 0

    def _place(self, x, y, board, tile):
        self.x = x
        self.y = y
        self.board = board
        self.tile = tile

    def _move(self, x, y, tile):
        self.x = x
        self.y = y
        self.tile = tile
        self.hasMoved = True
        self.moves += 1

    def draw(self):
        self.board.screen.blit(self.board.images[self.image], self.tile)

    def getMoves(self):
        moves = []
        for i in range(self.board.width):
            for j in range(self.board.height):
                if not self.board.isPiece(i, j):
                    moves.append((i, j))
        return moves
