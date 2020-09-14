from tkinter import *
from PIL import ImageTk, Image
from Pieces_.Pawn import Pawn
from Pieces_.Rook import Rook
from Pieces_.Queen import Queen
from Pieces_.Bishop import Bishop
from Pieces_.King import King
from Pieces_.Knight import Knight
from Pieces_.BlankPiece import Blank


def get_pieces_images():
    return {
        "BlackPawn": Pawn,
        "Pawn": Pawn,
        "BlackRook": Rook,
        "Rook": Rook,
        "BlackBishop": Bishop,
        "Bishop": Bishop,
        "BlackKing": King,
        "King": King,
        "BlackKnight": Knight,
        "Knight": Knight,
        "BlackQueen": Queen,
        "Queen": Queen,
        "0": Blank
    }
