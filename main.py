# import lib
import keyboard

# import .py
from interface import *
from dic_key import *
from search_word import *
from model_nextword.next_word import *
from keyboard_func import *

# switch
switch = 'on'

message = ""

# start the program
interface_text(" START ")

while switch == 'on':
    key = str(keyboard.read_event())
    print(key)
    print('[ Word ] : ' + message)
    if key[-5:] == 'down)':
        if key == 'KeyboardEvent(ctrl down)':
            pass
        else:
            message = message + key_string[key]
    
    # Reset message.
    if key in reset_key:
        print('[ Reset word ]')
        message = ""

    # Show prediction.
    # if keyboard.is_pressed('ctrl+space') == True :
    if key =='KeyboardEvent(ctrl down)':
        print('[ Word to predic ] : ' + message)
        if message == '':
            interface_text(" EMPTY ")
        else:
            # generate suggest word
            word_pred = search_word(message)
            num_nextword = 5 - len(word_pred)
            # generate next word
            next_word_list = next_word(message,num_nextword)

            option_list = word_pred + next_word_list
            # classify
            dic_option = {  'sug_word' : word_pred,
                            'next_word' : next_word_list}

            interface_predic(option_list)
  
    # Delete a word when pressing backspace.
    # if key == 'KeyboardEvent(backspace down)':
    if keyboard.is_pressed('backspace') == True :
        if message == "":
            pass
        else:
            message = message[:-1]

    # Select word by button.
    if key == 'KeyboardEvent(1 up)':
        click_button(0,message,option_list,dic_option)
        message = ""

    if key == 'KeyboardEvent(2 up)':
        click_button(1,message,option_list,dic_option)
        message = ""

    if key == 'KeyboardEvent(3 up)':
        click_button(2,message,option_list,dic_option)
        message = ""
    
    if key == 'KeyboardEvent(4 up)':
        click_button(3,message,option_list,dic_option)
        message = ""
    
    if key == 'KeyboardEvent(5 up)':
        click_button(4,message,option_list,dic_option)
        message = ""

    # Close the program.
    if key == 'KeyboardEvent(esc down)':
        print('[ Exit ]')
        interface_text(" EXIT ")
        message = ""
        key = ""
        switch = 'off'
