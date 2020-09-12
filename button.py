from tkinter import *


def createButton(frame, color, image, width, height, function):
    newButton = Button(frame, width=width, height=height, image=image,
                       bg=color, command=function)
    return newButton
