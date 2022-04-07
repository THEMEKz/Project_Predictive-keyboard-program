from tkinter import *
import tkinter.font as font

def interface_predic(word_):
    def close_window(event): 
        root.destroy()

    root = Tk()

    # on front
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    # root.iconify()
    root.update()
    root.deiconify()

    # set TK on center
    windowWidth = root.winfo_reqwidth()
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    root.geometry("+{}+{}".format(positionRight, 100))

    root.overrideredirect(True)

    root.bind("<Escape>", close_window)

    Font_style = font.Font(size=16)

    num = 0
    button_dict = {}
    for lang in word_:
        num = num + 1
        button_dict[lang] = Label(root,text=lang,borderwidth=0.5, relief="ridge")
        button_dict[lang]['font'] = Font_style
        root.bind(str(num),close_window)
        button_dict[lang].pack(side = LEFT,ipadx=30,ipady=10)

    root.mainloop()

def interface_text(text_):
    def close_window(): 
        root.destroy()

    root = Tk()
    root.overrideredirect(True)
    root.geometry('+860+80')

    root.lift()
    root.update()

    Font_style = font.Font(size=16)

    root.bind("<Escape>", close_window)

    A = Label(root,text=text_)
    A['font'] = Font_style
    A.pack(ipadx=30,ipady=10)
    
    root.after(500,close_window)
    root.mainloop()
