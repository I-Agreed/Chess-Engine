from engine.pieces.PieceBase import PieceBase


class Rook(PieceBase):
    def __init__(self, colour):
        super().__init__(colour)

    def getMoves(self):
        moves = []
        w = self.board.width
        h = self.board.height
        for i in range(self.x + 1, w):
            if not self.board.isPiece(i, self.y):
                moves.append((i, self.y))
            else:
                break
        for i in range(self.y + 1, h):
            if not self.board.isPiece(self.x, i):
                moves.append((self.x, i))
            else:
                break
        for i in range(self.x - 1, -1, -1):
            if not self.board.isPiece(i, self.y):
                moves.append((i, self.y))
            else:
                break
        for i in range(self.y - 1, -1, -1):
            if not self.board.isPiece(self.x, i):
                moves.append((self.x, i))
            else:
                break

        return moves
