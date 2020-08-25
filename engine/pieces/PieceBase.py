class PieceBase():
    piece = "base"
    def __init__(self, colour):
        self.x = None
        self.y = None
        self.board = None
        self.tile = None
        self.image = self.piece + "_" + colour
        self.colour = colour
        self.hasMoved = False
        self.moves = 0
        self.pawnEnPassantMove = -1

    def _place(self, x, y, board, tile):
        self.x = x
        self.y = y
        self.board = board
        self.tile = tile

    def _move(self, x, y, tile):
        self.x = x
        self.y = y
        if tile.piece is not None:
            self.board.pieces.remove(tile.piece)
        self.tile = tile
        self.hasMoved = True
        self.moves += 1

    def draw(self):
        self.board.screen.blit(self.board.images[self.image], self.tile)

    def getMoves(self, useInCheck=True):
        moves = []
        for i in range(self.board.width):
            for j in range(self.board.height):
                if not self.board.isPiece(i, j):
                    moves.append((i, j))
        return moves

    def isInCheck(self):
        return False
