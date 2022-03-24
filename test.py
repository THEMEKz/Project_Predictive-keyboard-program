# from model_nextword.next_word import *
# from interface import *
# r = 'word'
# print(next_word(r))


# root = Tk()
# root.overrideredirect(True)
# root.geometry('+860+80')
# def close_window(): 
#     root.destroy()

# Font_style = font.Font(size=16)

# root.bind("<Escape>", close_window)


# A1 = Label(root,text='num1')
# A1.pack(side = TOP,ipadx=30,ipady=3)

# A1 = Label(root,text='num1')
# A1.pack(side = LEFT,ipadx=30,ipady=3)

# A = Label(root,text='text_')
# A['font'] = Font_style
# A.pack(side = LEFT,ipadx=30,ipady=10)



# B = Label(root,text='text_')
# B['font'] = Font_style
# B.pack(side = LEFT,ipadx=30,ipady=10)

# import keyboard

# while True:
#     key = str(keyboard.read_event())
#     print(key)
#     if keyboard.is_pressed('ctrl+space') == True :
#         print('-----------------------')



# C = Label(root,text='text_')
# C['font'] = Font_style
# C.pack(side = LEFT,ipadx=30,ipady=10)
    
# root.after(5000,close_window)
# root.mainloop()
buggy_name = 'GeekflareE'
name = buggy_name.rstrip(buggy_name[-1])
print(name)