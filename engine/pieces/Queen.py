from engine.pieces.PieceBase import PieceBase

class Queen(PieceBase):
    def __init__(self, colour):
        super().__init__(colour)

    def getMoves(self):
        pass