from engine.pieces.PieceBase import PieceBase


class Knight(PieceBase):
    def __init__(self, colour):
        super().__init__(colour)

    def getMoves(self):
        moves = []

        for i in ((1, 2), (2, 1),
                  (-1, 2), (2, -1),
                  (1, -2), (-2, 1),
                  (-1, -2), (-2, -1)):
            x = self.x + i[0]
            y = self.y + i[1]
            if 0 <= x < self.board.width and \
               0 <= y < self.board.height:
                moves.append((x, y))

        return moves
