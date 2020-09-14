from tkinter import *

selected_piece = []


class Piece(Button):
    def __init__(self, master=None, image=None, chessBoard=None, width=64, height=64, selected=False, blank=False, pos=[]):
        self.image = image
        self.selected = selected
        self.chessBoard = chessBoard
        self.blank = blank
        self.position = pos
        super().__init__(master=master,
                         image=image,
                         width=width, height=height,
                         command=self.click)

    def find_selected_in_row(self, row):
        for col in range(8):
            if self.chessBoard[row[0]][col].selected:
                return True
        return False

    def click(self):
        self.selected_pieces = list(
            filter(self.find_selected_in_row, enumerate(self.chessBoard)))
        if len(list(
                filter(self.find_selected_in_row, enumerate(self.chessBoard)))) == 0:
            print("MOVE YOUR PIECE")
            self.selected = True
            selected_piece = self.position
        elif self.blank:
            print("PIECE MOVED")
            print(selected_piece)
            print(self.chessBoard[0][0])
