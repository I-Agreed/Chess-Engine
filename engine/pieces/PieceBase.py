class PieceBase():
    def __init__(self):
        self.x = None
        self.y = None
        self.board = None
        self.tile = None

    def _place(self, x, y, board, tile):
        self.x = x
        self.y = y
        self.board = board
        self.tile = tile

    def _move(self, x, y, tile):
        self.x = x
        self.y = y8
        self.tile = tile

    def draw(self):
        