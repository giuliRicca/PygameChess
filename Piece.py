from tkinter import *


class Piece(Button):
    def __init__(self, master=None, image=None, row=None, col=None):
        self.image = image
        self.row = row
        self.columns = col
        super().__init__(master=master, image=self.image, width=64, height=64)
