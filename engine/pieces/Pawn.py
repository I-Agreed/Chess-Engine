from engine.pieces.PieceBase import PieceBase


class Pawn(PieceBase):
    piece = "pawn"

    def __init__(self, colour):
        super().__init__(colour)

    def getMoves(self, useInCheck=True):
        direction = [1, -1][self.colour == "white"]
        moves = []
        if not self.board.isPiece(self.x, self.y + direction) and 0 <= self.y + direction < self.board.height:
            moves.append((self.x, self.y + direction))
            if not self.hasMoved and not self.board.isPiece(
               self.x, self.y + direction * 2) and 0 <= self.y + direction * 2 < self.board.height:
                moves.append((self.x, self.y + direction * 2))
        for i in (1, -1):
            if 0 <= self.y + direction < self.board.height and \
               0 <= self.x + i < self.board.width and self.board.isPiece(
               self.x + i, self.y + direction) and self.board.getPiece(
               self.x + i, self.y + direction).colour != self.colour:
                moves.append((self.x + i, self.y + direction))
        return moves
