from tkinter import *


def createButton(frame, color, image, width=64, height=64, function=None):
    newButton = Button(frame, width=width, height=height, image=image,
                       bg=color, command=function)
    return newButton
