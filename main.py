from tkinter import *
from chessBoard import Board
from button import createButton
from images import get_pieces_images
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


def movePiece(emprySlot, row, col):
    if currentPiece[2]:
        chessBoard[row][col].configure(image=currentPiece[0], width=64, height=64, command=lambda r=row,
                                       c=col, image=currentPiece[0]: getPiece(chessBoard[r][c], r, c, image))
        chessBoard[currentPiece[3]][currentPiece[4]].configure(image='', height=4, width=8, command=lambda: movePiece(
            chessBoard[currentPiece[1]][currentPiece[2]], currentPiece[3], currentPiece[4]))


# Define button
def createButton(frame, color, photo, w, h, command):
    b = Button(frame, width=w, height=h, image=photo,
               bg=color, command=command)
    return b


# Create Root
root = Tk()
root.geometry('600x600')
root.title("CHESS")

# Get Images
piece_images = get_pieces_images()
# CREATE BOARD
board = Board(root)
board.grid(row=0, column=0)
board.grid_propagate(0)
chessBoard = board.chessBoard
# DRAW BOARD
btnColor = '#27496d'
for row in range(8):
    for column in range(8):
        currentImage = chess[row][column]
        if currentImage == 'blackPawn':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            blackPieces.append(chessBoard[row][column])

        elif currentImage == 'pawn':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            whitePieces.append(chessBoard[row][column])

        elif currentImage == 'rook':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            whitePieces.append(chessBoard[row][column])

        elif currentImage == 'blackRook':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            blackPieces.append(chessBoard[row][column])

        elif currentImage == 'bishop':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            whitePieces.append(chessBoard[row][column])

        elif currentImage == 'blackBishop':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            blackPieces.append(chessBoard[row][column])

        elif currentImage == 'king':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            whitePieces.append(chessBoard[row][column])

        elif currentImage == 'blackKing':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            blackPieces.append(chessBoard[row][column])

        elif currentImage == 'knight':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            whitePieces.append(chessBoard[row][column])

        elif currentImage == 'blackKnight':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            blackPieces.append(chessBoard[row][column])

        elif currentImage == 'queen':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            whitePieces.append(chessBoard[row][column])

        elif currentImage == 'blackQueen':
            chessBoard[row].append(createButton(board, btnColor, piece_images[currentImage], 64, 64,
                                                command=lambda r=row, c=column, currentImg=piece_images[currentImage]:
                                                getPiece(chessBoard[r][c], r, c, currentImg)))
            blackPieces.append(chessBoard[row][column])

        else:
            chessBoard[row].append(createButton(board, btnColor, '', 8, 4,
                                                command=lambda r=row, c=column:
                                                movePiece(chessBoard[r][c], r, c)))

        chessBoard[row][column].place(
            x=board.slotWidth*column, y=board.slotHeight*row)

board.update()
root.mainloop()
