from engine.pieces.PieceBase import PieceBase


class Bishop(PieceBase):
    def __init__(self, colour):
        super().__init__(colour)

    def getMoves(self):
        size = min(self.board.height, self.board.width)
        moves = []
        for i in range(1, size - max(self.x, self.y)):
            x = self.x + i
            y = self.y + i
            if not self.board.isPiece(x, y):
                moves.append((x, y))
            elif self.board.getPiece(x, y).colour != self.colour:
                moves.append((x, y))
                break
            else:
                break
        for i in range(1, min(self.x, self.y) + 1):
            x = self.x - i
            y = self.y - i
            if not self.board.isPiece(x, y):
                moves.append((x, y))
            elif self.board.getPiece(x, y).colour != self.colour:
                moves.append((x, y))
                break
            else:
                break
        for i in range(1, min(size - self.x, self.y) + 1):
            x = self.x + i
            y = self.y - i
            if not self.board.isPiece(x, y):
                moves.append((x, y))
            elif self.board.getPiece(x, y).colour != self.colour:
                moves.append((x, y))
                break
            else:
                break
        for i in range(1, min(self.x, size - self.y) + 1):
            x = self.x - i
            y = self.y + i
            if not self.board.isPiece(x, y):
                print(1)
            elif self.board.getPiece(x, y).colour != self.colour:
                moves.append((x, y))
                break
            else:
                break

        return moves
