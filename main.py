# import lib
from time import sleep
import keyboard
from pyparsing import Word

# import .py
from interface import *
from dic_key import *
from search_word import *
from model_nextword.next_word import *

def press_backspace(list_string):
    for i in range(len(list_string,)):
        print('[ Delete ] : '+list_string[-(i+1)])
        sleep(0.001)
        keyboard.press('backspace')


def write_word(word_select):
    print('[ Select word ] : ' + word_select)
 
    print('[ Write word ] : ' + word_select)
    keyboard.write(word_select)

interface_text(" START ")

# L = ['A','B','C']
next_word_list = []
mode = 'pred'
# switch
P = 'On'

list_string = ''
record_string = ''

while P == 'On':
    key = str(keyboard.read_event())
    print(key)
    print('[ Word ] : ' + list_string)
    print('[ Record ] : ' + record_string)
    if key[-5:] == 'down)':
        if key == 'KeyboardEvent(ctrl down)':
            pass
        else:
            record_string = record_string + key_string_2[key]
            list_string = list_string + key_string[key]
    
    # reset with space
    if key in key_func:
        print('[ Reset word ]')
        list_string = ""

    # call interface
    # if keyboard.is_pressed('ctrl+space') == True :
    if key =='KeyboardEvent(ctrl down)':
        print('[ Word to predic ] : ' + list_string)
        if list_string == '':
            interface_text(" EMPTY ")
        else:
            # predic word

            word_pred = search_word(list_string)
            num_nextword = 5 - len(word_pred)

            next_word_list = next_word(list_string,num_nextword)

            option_list = word_pred + next_word_list

            dic_option = { 'sug_word' : word_pred,
                            'next_word' : next_word_list}

            interface_predic(option_list)
  
    # backspace
    # if key == 'KeyboardEvent(backspace down)':
    if keyboard.is_pressed('backspace') == True :
        if list_string == '':
            pass
        else:
            # if record_string[:-1] == " " :
            # print(len(record_string))
            record_string = record_string[:-1]
            # else:
                # record_string = record_string.rstrip(record_string[-1])
            # record_string = record_string[:-2]
            list_string = list_string[:-1]

    # set key to write word
    if key == 'KeyboardEvent(1 up)':
        if list_string == "":
            pass
        else:
            if option_list[0] in dic_option['next_word']:
                keyboard.press('space')
            if option_list[0] in dic_option['sug_word']:
                press_backspace(list_string)

            write_word(option_list[0])
            list_string = ""

    if key == 'KeyboardEvent(2 up)':
        if list_string == "":
            pass
        else:
            if option_list[1] in dic_option['next_word']:
                keyboard.press('space')
            if option_list[1] in dic_option['sug_word']:
                press_backspace(list_string)
     
            write_word(option_list[1])
            list_string = ""

    if key == 'KeyboardEvent(3 up)':
        if list_string == "":
            pass
        else:
            if option_list[2] in dic_option['next_word']:
                keyboard.press('space')
            if option_list[2] in dic_option['sug_word']:
                press_backspace(list_string)
        
            write_word(option_list[2])
            list_string = ""
    
    if key == 'KeyboardEvent(4 up)':
        if list_string == "":
            pass
        else:
            if option_list[3] in dic_option['next_word']:
                keyboard.press('space')
            if option_list[3] in dic_option['sug_word']:
                press_backspace(list_string)
       
            write_word(option_list[3])
            list_string = ""
    
    if key == 'KeyboardEvent(5 up)':
        if list_string == "":
            pass
        else:
            if option_list[4] in dic_option['next_word']:
                keyboard.press('space')
            if option_list[4] in dic_option['sug_word']:
                press_backspace(list_string)
         
            write_word(option_list[4])
            list_string = ""

    # exit loop
    if key == 'KeyboardEvent(esc down)':
        print('[ Exit ]')
        interface_text(" EXIT ")
        list_string = ""
        key = ''
        P = 'Off'
