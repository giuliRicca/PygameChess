from tkinter import *
from PIL import ImageTk, Image

app = Tk()
app.title('image')
app.geometry('300x300')

img=Image.open("pieces/blackPawn.png")
photo = ImageTk.PhotoImage(img)
button = Button(app,image=photo)
button.grid(row=0,column=0)

app.mainloop()