from engine.pieces.PieceBase import PieceBase


class Pawn(PieceBase):
    def __init__(self, colour):
        super().__init__(colour)

    def getMoves(self, useInCheck=True):
        direction = [1, -1][self.colour == "white"]
        moves = []
        if not self.board.isPiece((self.x, self.y + direction)):
            moves.append((self.x, self.y + direction))
        if not self.hasMoved and self.board.isPiece((self.x, self.y + direction * 2)):
            moves.append((self.x, self.y + direction * 2))
        for i in (1, -1):
            if self.board.isPiece((self.x + i, self.y + direction)) and board.getPiece(
                                  (self.x + i, self.y + direction)).colour != self.colour:
                moves.append((self.x + i, self.y + direction))
