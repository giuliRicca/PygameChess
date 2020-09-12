from Piece import Piece
from PIL import ImageTk, Image


class Queen(Piece):
    def __init__(self, master=None, row=None):
        self.black = False
        self.row = row
        self.set_color_by_row()
        self.columns = [0, 7]
        super().__init__(master=master, image=self.image,
                         row=self.row, col=self.columns)

    def set_color_by_row(self):
        if self.row == 0:
            self.row = [7]
            self.image = ImageTk.PhotoImage(
                Image.open("pieces/blackQueen.png"))
            return
        else:
            self.row = [1]
            self.image = ImageTk.PhotoImage(Image.open("pieces/queen.png")),
