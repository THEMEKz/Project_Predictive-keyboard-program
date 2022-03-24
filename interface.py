from tkinter import *
import tkinter.font as font

def interface_predic(word_):
    def close_window(event): 
        root.destroy()

    root = Tk()

    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)

    root.iconify()
    root.update()
    root.deiconify()

    root.overrideredirect(True)
    root.geometry('+860+80')
    Font_style = font.Font(size=16)

    root.bind("<Escape>", close_window)

    num = 0
    button_dict = {}
    for lang in word_:
        num = num + 1
        button_dict[lang] = Label(root,text=lang,borderwidth=0.5, relief="ridge")
        button_dict[lang]['font'] = Font_style
        root.bind(str(num),close_window)
        button_dict[lang].pack(side = LEFT,ipadx=30,ipady=10)

    # A = Label(root,text=lang,bg="#24292e",fg="white")

    # l1 = Label(root,text=word_[0])
    # l1['font'] = Font_style
    # root.bind("1",close_window)
    # l1.pack(side = LEFT,ipadx=30,ipady=10)

    root.mainloop()

def interface_text(text_):
    def close_window(): 
        root.destroy()

    root = Tk()
    root.overrideredirect(True)
    root.geometry('+860+80')

    Font_style = font.Font(size=16)

    root.bind("<Escape>", close_window)

    A = Label(root,text=text_)
    A['font'] = Font_style
    A.pack(ipadx=30,ipady=10)
    
    root.after(500,close_window)
    root.mainloop()
