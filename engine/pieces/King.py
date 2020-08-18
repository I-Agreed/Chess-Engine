from engine.pieces.PieceBase import PieceBase


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