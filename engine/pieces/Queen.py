from engine.pieces.PieceBase import PieceBase

class Queen(PieceBase):
    def __init__(self, colour):
        super().__init__(colour)

    def getMoves(self):
        moves = []
        w = self.board.width
        h = self.board.height
        size = min(self.board.height, self.board.width)
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
        for i in range(1, size - max(self.x, self.y)):
            x = self.x + i
            y = self.y + i
            if not self.board.isPiece(x, y):
                moves.append((x, y))
            else:
                break
        for i in range(1, min(self.x, self.y)+1):
            x = self.x - i
            y = self.y - i
            if not self.board.isPiece(x, y):
                moves.append((x, y))
            else:
                break
        for i in range(-1, min(size - self.x, self.y)):
            x = self.x + i
            y = self.y - i
            if not self.board.isPiece(x, y):
                moves.append((x, y))
            else:
                break
        for i in range(-1, min(self.x, size - self.y)):
            x = self.x - i
            y = self.y + i
            if not self.board.isPiece(x, y):
                moves.append((x, y))
            else:
                break
        return moves
