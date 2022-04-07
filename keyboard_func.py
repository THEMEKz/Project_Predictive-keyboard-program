import keyboard
from time import sleep

def press_backspace(list_string):
    for i in range(len(list_string,)):
        print('[ Delete ] : '+list_string[-(i+1)])
        sleep(0.001)
        keyboard.press('backspace')

def write_word(word_select):
    print('[ Select word ] : ' + word_select)
 
    print('[ Write word ] : ' + word_select)
    keyboard.write(word_select)

def click_button(bt,message,option_list,dic_option):
    if message == "":
            pass
    else:
        if option_list[bt] in dic_option['next_word']:
            keyboard.press('space')
        if option_list[bt] in dic_option['sug_word']:
            press_backspace(message)
         
        write_word(option_list[bt])