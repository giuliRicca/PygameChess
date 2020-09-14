from Piece import Piece


class Blank(Piece):
    def __init__(self, master=None, row=None, col=None, command=None, chessBoard=None):
        self.row = row
        self.col = col
        self.selected = False
        self.blank = True
        super().__init__(master=master, chessBoard=chessBoard,
                         width=8, height=4, selected=self.selected, blank=self.blank)
