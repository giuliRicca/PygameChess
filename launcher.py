from tkinter import *
from ChessBoard import Board


class Launcher:
    def __init__(self, root):
        self.root = root

        self.initUI()
        self.root.title("chess")
        self.root.mainloop()

    def initUI(self):
        board = Board(self.root)


root = Tk()

if __name__ == "__main__":
    launcher = Launcher(root)
