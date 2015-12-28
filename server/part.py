from piece import Piece

class Part:
    def __init__(self, piece=Piece.none, is_white=None):
        self.piece = piece
        self.is_white = is_white
