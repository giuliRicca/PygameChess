from Piece import Piece
from PIL import ImageTk, Image


class Pawn(Piece):
    def __init__(self, master=None, row=None):
        self.black = False
        self.row = row
        self.set_color_by_row()
        self.columns = [n for n in range(8)]
        super().__init__(master=master, image=self.image,
                         row=self.row, col=self.columns)

    def set_color_by_row(self):
        if self.row == 1:
            self.row = [6]
            self.image = ImageTk.PhotoImage(Image.open("pieces/blackPawn.png"))
            return
        else:
            self.row = [1]
            self.image = ImageTk.PhotoImage(Image.open("pieces/pawn.png")),
