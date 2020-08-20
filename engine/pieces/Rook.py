from engine.pieces.PieceBase import PieceBase


class Rook(PieceBase):
    def __init__(self, colour):
        super().__init__(colour)

    def getMoves(self, useInCheck=True):
        moves = []
        w = self.board.width
        h = self.board.height
        for i in range(self.x + 1, w):
            if not self.board.isPiece(i, self.y):
                moves.append((i, self.y))
            else:
                if self.board.getPiece(i, self.y).colour != self.colour:
                    moves.append((i, self.y))
                break
        for i in range(self.y + 1, h):
            if not self.board.isPiece(self.x, i):
                moves.append((self.x, i))
            else:
                if self.board.getPiece(self.x, i).colour != self.colour:
                    moves.append((self.x, i))
                break
        for i in range(self.x - 1, -1, -1):
            if not self.board.isPiece(i, self.y):
                moves.append((i, self.y))
            else:
                if self.board.getPiece(i, self.y).colour != self.colour:
                    moves.append((i, self.y))
                break
        for i in range(self.y - 1, -1, -1):
            if not self.board.isPiece(self.x, i):
                moves.append((self.x, i))
            else:
                if self.board.getPiece(self.x, i).colour != self.colour:
                    moves.append((self.x, i))
                break
        if useInCheck:
            kingMoves = self.board.getKing(self.colour).isInCheck()
            if kingMoves:
                moves = filter(lambda i: i in kingMoves, moves)
        return moves
