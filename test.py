from tkinter import *
import tkinter.font as font
from turtle import color


def interface_text(text_):
    def close_window(): 
        root.destroy()

    def lossfocus(event):
        if event.widget is root: # check which widget getting the focus 
            w = root.tk.call('focus')
            if not w: # not widget in this window 
                root.destroy()

    root = Tk()

    root.bind("<Button-1>", lossfocus)
    root.overrideredirect(True)
    root.geometry('+860+80')
    root.lift()
    root.update()
    
    Font_style = font.Font(size=16)

    root.bind("<Escape>", close_window)

    A = Label(root,text=text_)
    A['font'] = Font_style
    A.pack(ipadx=30,ipady=10)
    
    root.after(5000,close_window)
    root.mainloop()

interface_text(" EXIT ")