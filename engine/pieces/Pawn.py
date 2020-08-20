from engine.pieces.PieceBase import PieceBase

class Pawn(PieceBase):
    def __init__(self, colour):
        super().__init__(colour)

    def getMoves(self, useInCheck=True):
        pass