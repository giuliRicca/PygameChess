from tkinter import *
from ChessBoard import Board
from Button import createButton
from Images import get_pieces_images
from PIL import ImageTk, Image

# CHESS BOARD
chess = [['blackRook', 'blackKnight', 'blackBishop', 'blackQueen', 'blackKing', 'blackBishop', 'blackKnight', 'blackRook'],
         ['blackPawn', 'blackPawn', 'blackPawn', 'blackPawn',
          'blackPawn', 'blackPawn', 'blackPawn', 'blackPawn'],
         [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [
    0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
    ['pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'],
    ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']]


currentPiece = [0, 0, False]
blackPieces = []
whitePieces = []


def getPiece(piece, row, col, image):
    global currentPiece
    if not currentPiece[2] and chessBoard[row][col] != 0:
        currentPiece = [image, piece, True, row, col]
    else:
        chessBoard[row][col].configure(image=currentPiece[0], width=64, height=64, command=lambda r=row,
                                       c=col, image=currentPiece[0]: getPiece(chessBoard[r][c], r, c, image))
        chessBoard[currentPiece[3]][currentPiece[4]].configure(image='', height=4, width=8, command=lambda: movePiece(
            chessBoard[currentPiece[1]][currentPiece[2]], currentPiece[3], currentPiece[4]))


root = Tk()
root.geometry('600x600')
root.title("CHESS")

piece_images = get_pieces_images()

board = Board(root)
board.grid(row=0, column=0)
board.grid_propagate(0)
emptyBoard = board.chessBoard


def renderChessBoard(row):
    for i in range(8):
        btnColor = '#27496d'
        if (row[0] % 2 == 0 and i % 2 == 0) or (row[0] % 2 != 0 and i % 2 != 0):
            btnColor = '#fff'

        currentImage = chess[row[0]][i]
        currentImage = piece_images[currentImage]
        row[1].append(createButton(board, btnColor,
                                   currentImage,
                                   function=lambda row=row[0], column=i:
                                   getPiece(chessBoard[row][column], row, column, currentImage)))

        row[1][i].place(x=board.slotWidth*i, y=board.slotHeight*row[0])

    return row[1]


chessBoard = list(map(renderChessBoard, enumerate(emptyBoard)))

board.update()
root.mainloop()
