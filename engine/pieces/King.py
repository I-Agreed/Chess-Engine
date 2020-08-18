from engine.pieces.PieceBase import PieceBase
from engine.pieces import Bishop
from engine.pieces import Rook
from engine.pieces import Queen
from engine.pieces import Knight
from engine.pieces import Pawn


class King(PieceBase):
    def __init__(self, colour):
        super().__init__(colour)

    def isInCheck(self):
        # TODO: Check all directions and knight jumps from the king
        pass

    def getMoves(self):
        moves = []
        enemyMoves = []
        x = self.x
        y = self.y
        for i in self.board.getPieces(["black", "white"][self.colour == "black"]):
            for j in i.getMoves():
                enemyMoves.append(j)
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.board.width and \
                        0 <= y + j < self.board.height:
                    if not self.board.isPiece(x + i, y + j) and (x + i, y + j) not in enemyMoves:
                        moves.append((x + i, y + j))
        return moves

    def isInCheck(self):
        size = min(self.board.height, self.board.width)
        out = False
        for i in range(1, size - max(self.x, self.y)):
            x = self.x + i
            y = self.y + i
            if not self.board.isPiece(x, y) and not out:
                pass
            elif self.board.getPiece(x, y).colour != self.colour and not out:
                if type(self.board.getPiece(x, y)) in (Queen.Queen, Bishop.Bishop):
                    out = True
                break
            else:
                break
        for i in range(1, min(self.x, self.y) + 1):
            x = self.x - i
            y = self.y - i
            if not self.board.isPiece(x, y) and not out:
                pass
            elif self.board.getPiece(x, y).colour != self.colour and not out:
                if type(self.board.getPiece(x, y)) in (Queen.Queen, Bishop.Bishop):
                    out = True
                break
            else:
                break
        for i in range(1, min(size - self.x, self.y)):
            x = self.x + i
            y = self.y - i
            if not self.board.isPiece(x, y) and not out:
                pass
            elif self.board.getPiece(x, y).colour != self.colour and not out:
                if type(self.board.getPiece(x, y)) in (Queen.Queen, Bishop.Bishop):
                    out = True
                break
            else:
                break
        for i in range(1, min(self.x, size - self.y)):
            x = self.x - i
            y = self.y + i
            if not self.board.isPiece(x, y) and not out:
                pass
            elif self.board.getPiece(x, y).colour != self.colour and not out:
                if type(self.board.getPiece(x, y)) in (Queen.Queen, Bishop.Bishop):
                    out = True
                break
            else:
                break
        # ROOK
        w = self.board.width
        h = self.board.height
        if not out:
            for i in range(self.x + 1, w):
                if not self.board.isPiece(i, self.y) and not out:
                    pass
                else:
                    if self.board.getPiece(i, self.y).colour != self.colour and type(
                            self.board.getPiece(i, self.y)) == Rook.Rook and not True:
                        out = True
                    break
            for i in range(self.y + 1, h):
                if not self.board.isPiece(self.x, i):
                    pass
                else:
                    if self.board.getPiece(self.x, i).colour != self.colour and type(
                            self.board.getPiece(self.x, i)) == Rook.Rook and not True:
                        out = True
                    break
            for i in range(self.x - 1, -1, -1):
                if not self.board.isPiece(i, self.y):
                    pass
                else:
                    if self.board.getPiece(i, self.y).colour != self.colour and type(
                            self.board.getPiece(i, self.y)) == Rook.Rook and not True:
                        out = True
                    break
            for i in range(self.y - 1, -1, -1):
                if not self.board.isPiece(self.x, i):
                    pass
                else:
                    if self.board.getPiece(self.x, i).colour != self.colour and type(
                            self.board.getPiece(self.x, i)) == Rook.Rook and not True:
                        out = True
                    break
        for i in ((1, 2), (2, 1),
                  (-1, 2), (2, -1),
                  (1, -2), (-2, 1),
                  (-1, -2), (-2, -1)):
            x = self.x + i[0]
            y = self.y + i[1]
            if 0 <= x < self.board.width and \
                    0 <= y < self.board.height:
                if self.board.isPiece(x, y) and self.board.getPiece(x, y).colour != self.colour and type(
                   self.board.getPiece(x, y)) == Knight.Knight:
                    out = True
        for i in (((1, -1), (-1, -1)), ((1, 1), (-1, 1)))[self.colour == "black"]:
            x = self.x + i[0]
            y = self.y + i[1]
            if 0 <= x < self.board.width and \
                    0 <= y < self.board.height:
                if self.board.isPiece(x, y) and self.board.getPiece(x, y).colour != self.colour and type(
                   self.board.getPiece(x, y)) == Pawn.Pawn:
                    out = True
        return out