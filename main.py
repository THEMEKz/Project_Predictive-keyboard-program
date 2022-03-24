# import lib
from time import sleep
import keyboard
from pyparsing import Word

# import .py
from interface import *
from dic_key import *
from search_word import *


def write_word(list_string,word_select):
    print('[ Select word ] : ' + word_select)
    for i in range(len(list_string,)):
            print('[ Delete ] : '+list_string[-(i+1)])
            sleep(0.001)
            keyboard.press('backspace')
   
    print('[ Write word ] : ' + word_select)
    keyboard.write(word_select)

interface_text(" START ")

# switch
P = 'On'

list_string = ''

while P == 'On':
    key = str(keyboard.read_event())
    print(key)
    print('[ Word ] : ' + list_string)
    if key[-5:] == 'down)':
        if key == 'KeyboardEvent(ctrl down)':
            pass
        else:
            list_string = list_string + key_string[key]
    
    # reset with space
    if key in key_func:
        print('[ Reset word ]')
        list_string = ""

    # call interface
    if key =='KeyboardEvent(ctrl down)':
        print('[ Word to predic ] : ' + list_string)
        if list_string == '':
            interface_text(" EMPTY ")
        else:
            # predic word
            word_pred = search_word(list_string)
            word_1,word_2,word_3 = word_pred

            interface_predic(word_pred)
            
    # backspace
    if key == 'KeyboardEvent(backspace down)':
        if list_string == '':
            pass
        else:
            list_string = list_string[:-1:]

    # set key to write word
    if key == 'KeyboardEvent(1 up)':
        if list_string == "":
            pass
        else:
            write_word(list_string,word_1)
            list_string = ""
    
    if key == 'KeyboardEvent(2 up)':
        if list_string == "":
            pass
        else:
            write_word(list_string,word_2)
            list_string = ""

    if key == 'KeyboardEvent(3 up)':
        if list_string == "":
            pass
        else:
            write_word(list_string,word_3)
            list_string = ""
    
    # exit loop
    if key == 'KeyboardEvent(esc down)':
        print('[ Exit ]')
        interface_text(" EXIT ")
        list_string = ""
        key = ''
        P = 'Off'
