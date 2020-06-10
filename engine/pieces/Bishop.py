from engine.pieces.PieceBase import PieceBase

class Bishop(PieceBase):
    def __init__(self, colour):
        super().__init__(colour)

    def getMoves(self):
        size = min(self.board.height, self.board.width)
        moves = []
        for i in range(1, size-max(self.x, self.y)):
            x = self.x + i
            y = self.y + i
            if not self.board.isPiece(x, y):
                moves.append((x, y))
            else:
                break
        return moves