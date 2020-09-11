from tkinter import *

# BOARD CLASS


class Board(Frame):
    def __init__(self, root, slotWidth=64, slotHeight=64):
        self.b = [[], [], [], [], [], [], [], []]
        self.root = root
        self.slotWidth = slotWidth
        self.slotHeight = slotHeight
        self.width = slotWidth*8
        self.height = slotHeight*8
        Frame.__init__(self, root, width=self.width, height=self.height)
