from Piece import Piece
from PIL import ImageTk, Image


class Pawn(Piece):
    def __init__(self, master=None, row=None, col=None, chessBoard=None, selected=False):
        self.black = False
        self.position = [row, col]
        self.chessBoard = chessBoard
        self.set_row_by_color()

        self.selected = selected
        super().__init__(master=master, image=self.image,
                         chessBoard=self.chessBoard, selected=self.selected, pos=self.position)

    def set_row_by_color(self):
        if self.position[0] == 1:
            self.image = ImageTk.PhotoImage(Image.open("pieces/blackPawn.png"))
            return
        else:
            self.image = ImageTk.PhotoImage(Image.open("pieces/pawn.png"))
