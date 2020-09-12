from tkinter import *
from Pieces_.Pawn import Pawn
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
        self.piece_types = get_pieces_images(self.root)

        self.initUI()

        Frame.__init__(self, root, width=self.width, height=self.height)

    def initUI(self):
        self.chessBoard = [[] for i in range(len(self.chess))]
        self.chessBoard = list(
            map(self.render_row, enumerate(self.chessBoard)))

        self.populate_chess_board()
        self.chessBoard = list(
            map(self.render_row, enumerate(self.chessBoard)))

    def render_row(self, chess_row):
        return list(map(lambda button:
                        button[1].grid(row=chess_row[0],
                                       column=button[0]),
                        enumerate(chess_row[1])))

    def populate_chess_board(self):
        for row in range(len(self.chessBoard)):
            for col in range(len(self.chessBoard)):
                currentImage = self.chess[row][col]
                if currentImage in self.piece_types:
                    self.chessBoard[row].append(
                        self.piece_types[currentImage](self.root, row=row))
                else:
                    self.chessBoard[row].append(
                        Button(self.root, width=8, height=4))
