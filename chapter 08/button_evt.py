from tkinter import *

def callback():
    button["text"] ="버튼이 클릭되었음!"

root = Tk()

button = Button(root, text="클릭", command=callback)
button.pack(side=LEFT)

root.mainloop()