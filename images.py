from tkinter import *
from PIL import ImageTk, Image


def get_pieces_images():
    return {
        "blackPawn": ImageTk.PhotoImage(Image.open("pieces/blackPawn.png")),
        "pawn": ImageTk.PhotoImage(Image.open("pieces/pawn.png")),
        "blackRook": ImageTk.PhotoImage(Image.open("pieces/blackTower.png")),
        "rook": ImageTk.PhotoImage(Image.open("pieces/tower.png")),
        "blackBishop": ImageTk.PhotoImage(Image.open("pieces/blackBishop.png")),
        "bishop": ImageTk.PhotoImage(Image.open("pieces/bishop.png")),
        "blackKing": ImageTk.PhotoImage(Image.open("pieces/blackKing.png")),
        "king": ImageTk.PhotoImage(Image.open("pieces/king.png")),
        "blackKnight": ImageTk.PhotoImage(Image.open("pieces/blackKnight.png")),
        "knight": ImageTk.PhotoImage(Image.open("pieces/knight.png")),
        "blackQueen": ImageTk.PhotoImage(Image.open("pieces/blackQueen.png")),
        "queen": ImageTk.PhotoImage(Image.open("pieces/queen.png")),
        0: "",
    }
