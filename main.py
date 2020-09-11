from tkinter import *
from chessBoard import Board
from PIL import ImageTk, Image

# CHESS BOARD
chessBoard = [['blackRook', 'blackKnight', 'blackBishop', 'blackQueen', 'blackKing', 'blackBishop', 'blackKnight', 'blackRook'],
              ['blackPawn', 'blackPawn', 'blackPawn', 'blackPawn', 'blackPawn', 'blackPawn', 'blackPawn', 'blackPawn'], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], ['pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn'], ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']]

# MOVE PIECE
currentPiece = [0, 0, False]
blackPieces = []
whitePieces = []


def getPiece(piece, row, col, image):
    global currentPiece
    if not currentPiece[2] and chessBoard[row][col] != 0:
        currentPiece = [image, piece, True, row, col]


def movePiece(blankPiece, row, col):
    if currentPiece[2]:
        b[row][col].configure(image=currentPiece[0], width=64, height=64, command=lambda r=row,
                              c=col, image=currentPiece[0]: getPiece(b[r][c], r, c, image))
        b[currentPiece[3]][currentPiece[4]].configure(image='', height=4, width=8, command=lambda: movePiece(
            b[currentPiece[1]][currentPiece[2]], currentPiece[3], currentPiece[4]))


# Define button
def button(frame, color, photo, w, h, command):
    b = Button(frame, width=w, height=h, image=photo,
               bg=color, command=command)
    return b


# CREATE SCREEN
root = Tk()
root.geometry('600x600')
root.title("CHESS")

# IMAGE PATH
blackPawn = ImageTk.PhotoImage(Image.open("pieces/blackPawn.png"))
pawn = ImageTk.PhotoImage(Image.open("pieces/pawn.png"))
blackRook = ImageTk.PhotoImage(Image.open("pieces/blackTower.png"))
rook = ImageTk.PhotoImage(Image.open("pieces/tower.png"))
blackBishop = ImageTk.PhotoImage(Image.open("pieces/blackBishop.png"))
bishop = ImageTk.PhotoImage(Image.open("pieces/bishop.png"))
blackKing = ImageTk.PhotoImage(Image.open("pieces/blackKing.png"))
king = ImageTk.PhotoImage(Image.open("pieces/king.png"))
blackKnight = ImageTk.PhotoImage(Image.open("pieces/blackKnight.png"))
knight = ImageTk.PhotoImage(Image.open("pieces/knight.png"))
blackQueen = ImageTk.PhotoImage(Image.open("pieces/blackQueen.png"))
queen = ImageTk.PhotoImage(Image.open("pieces/queen.png"))
# CREATE BOARD
board = Board(root)
board.grid(row=0, column=0)
board.grid_propagate(0)
b = board.b
# DRAW BOARD
btnColor = '#27496d'
for row in range(8):
    for column in range(8):
        currentImage = chessBoard[row][column]
        if currentImage == 'blackPawn':
            b[row].append(button(board, btnColor, blackPawn, 64, 64,
                                 command=lambda r=row, c=column: getPiece(b[r][c], r, c, blackPawn)))
            blackPieces.append(b[row][column])

        elif currentImage == 'pawn':
            b[row].append(button(board, btnColor, pawn, 64, 64,
                                 command=lambda r=row, c=column: getPiece(b[r][c], r, c, pawn)))
            whitePieces.append(b[row][column])

        elif currentImage == 'rook':
            b[row].append(button(board, btnColor, rook, 64, 64,
                                 command=lambda r=row, c=column: getPiece(b[r][c], r, c, rook)))
            whitePieces.append(b[row][column])

        elif currentImage == 'blackRook':
            b[row].append(button(board, btnColor, blackRook, 64, 64,
                                 command=lambda r=row, c=column: getPiece(b[r][c], r, c, blackRook)))
            blackPieces.append(b[row][column])

        elif currentImage == 'bishop':
            b[row].append(button(board, btnColor, bishop, 64, 64,
                                 command=lambda r=row, c=column: getPiece(b[r][c], r, c, bishop)))
            whitePieces.append(b[row][column])

        elif currentImage == 'blackBishop':
            b[row].append(button(board, btnColor, blackBishop, 64, 64,
                                 command=lambda r=row, c=column: getPiece(b[r][c], r, c, blackBishop)))
            blackPieces.append(b[row][column])

        elif currentImage == 'king':
            b[row].append(button(board, btnColor, king, 64, 64,
                                 command=lambda r=row, c=column: getPiece(b[r][c], r, c, king)))
            whitePieces.append(b[row][column])

        elif currentImage == 'blackKing':
            b[row].append(button(board, btnColor, blackKing, 64, 64,
                                 command=lambda r=row, c=column: getPiece(b[r][c], r, c, blackKing)))
            blackPieces.append(b[row][column])

        elif currentImage == 'knight':
            b[row].append(button(board, btnColor, knight, 64, 64,
                                 command=lambda r=row, c=column: getPiece(b[r][c], r, c, knight)))
            whitePieces.append(b[row][column])

        elif currentImage == 'blackKnight':
            b[row].append(button(board, btnColor, blackKnight, 64, 64,
                                 command=lambda r=row, c=column: getPiece(b[r][c], r, c, blackKnight)))
            blackPieces.append(b[row][column])

        elif currentImage == 'queen':
            b[row].append(button(board, btnColor, queen, 64, 64,
                                 command=lambda r=row, c=column: getPiece(b[r][c], r, c, queen)))
            whitePieces.append(b[row][column])

        elif currentImage == 'blackQueen':
            b[row].append(button(board, btnColor, blackQueen, 64, 64, command=lambda r=row,
                                 c=column, i='blackQueen': getPiece(b[r][c], r, c, blackQueen)))
            blackPieces.append(b[row][column])

        else:
            b[row].append(button(board, btnColor, '', 8, 4,
                                 command=lambda r=row, c=column: movePiece(b[r][c], r, c)))

        b[row][column].place(x=board.slotWidth*column, y=board.slotHeight*row)

board.update()
root.mainloop()
