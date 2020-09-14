from tkinter import *
from Pieces import get_pieces_images
# BOARD CLASS
chess = [['BlackRook', 'BlackKnight', 'BlackBishop', 'BlackQueen', 'BlackKing', 'BlackBishop', 'BlackKnight', 'BlackRook'],
         ['BlackPawn', 'BlackPawn', 'BlackPawn', 'BlackPawn',
          'BlackPawn', 'BlackPawn', 'BlackPawn', 'BlackPawn'],
         ['0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'], [
    '0', '0', '0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0', '0', '0'],
    ['Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn', 'Pawn'],
    ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook']]


class Board(Frame):
    def __init__(self, root, slotWidth=64, slotHeight=64):
        self.root = root
        self.slotWidth = slotWidth
        self.slotHeight = slotHeight
        self.width = slotWidth*8
        self.height = slotHeight*8
        self.chess = chess
        self.piece_types = get_pieces_images()
        self.initUI()

        Frame.__init__(self, root, width=self.width, height=self.height)

    def initUI(self):
        self.chessBoard = [[] for i in range(len(self.chess))]
        self.chessBoard = list(
            map(self.populate_row, enumerate(self.chessBoard)))
        self.selected_pieces = list(
            filter(self.find_selected_in_row, enumerate(self.chessBoard)))

    def populate_row(self, row):
        for column in range(8):
            row[1].append(self.piece_types[chess[row[0]][column]](
                self.root, row=row[0], col=column))
            row[1][column].grid(row=row[0], column=column)
        return row[1]

    def find_selected_in_row(self, row):
        for col in range(8):
            self.chessBoard[row[0]][col].chessBoard = self.chessBoard
            if self.chessBoard[row[0]][col].selected:
                return True
        return False
