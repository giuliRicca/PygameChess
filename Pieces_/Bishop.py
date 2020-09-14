from Piece import Piece
from PIL import ImageTk, Image


class Bishop(Piece):
    def __init__(self, master=None, row=None, col=None, chessBoard=None):
        self.black = False
        self.row = row
        self.col = col
        self.selected = False
        self.set_color_by_row()
        super().__init__(master=master, image=self.image)

    def set_color_by_row(self):
        if self.row == 0:
            self.row = [7]
            self.image = ImageTk.PhotoImage(
                Image.open("pieces/blackBishop.png"))
            return
        else:
            self.row = [1]
            self.image = ImageTk.PhotoImage(Image.open("pieces/bishop.png")),
