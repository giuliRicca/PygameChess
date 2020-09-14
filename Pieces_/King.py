from Piece import Piece
from PIL import ImageTk, Image


class King(Piece):
    def __init__(self, master=None, row=None, col=None, chessBoard=None):
        self.black = False
        self.row = row
        self.set_color_by_row()
        self.col = col
        self.selected = False
        super().__init__(master=master, image=self.image)

    def set_color_by_row(self):
        if self.row == 0:
            self.row = [7]
            self.image = ImageTk.PhotoImage(
                Image.open("pieces/blackKing.png"))
            return
        else:
            self.row = [1]
            self.image = ImageTk.PhotoImage(Image.open("pieces/king.png")),
