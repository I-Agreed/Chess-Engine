from engine.pieces.PieceBase import PieceBase


class Pawn(PieceBase):
    piece = "pawn"

    def __init__(self, colour):
        super().__init__(colour)

    def _move(self, x, y, tile):
        if abs(self.y-y) == 2:
            self.pawnEnPassantMove = self.board.turnNum
        if self.x != x and not self.board.isPiece(x, y):
            self.board.tiles[x][self.y] = None
            if self.board.tiles[x][self.y] is not None:
                self.board.pieces.remove(tile.piece)
        self.x = x
        self.y = y
        self.tile = tile
        self.hasMoved = True
        self.moves += 1

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
            if 0 <= self.y + direction < self.board.width and \
               0 <= self.x + i < self.board.width and self.board.isPiece(
               self.x + i, self.y) and self.board.getPiece(
               self.x + i, self.y).colour != self.colour and \
               type(self.board.getPiece(self.x + i, self.y)) is type(self) and \
               self.board.getPiece(self.x + i, self.y).pawnEnPassantMove == self.board.turnNum-1:
                moves.append((self.x + i, self.y + direction))
        return moves
