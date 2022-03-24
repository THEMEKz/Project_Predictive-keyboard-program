import json

def search_word(word):
    word_token = json.load(open('token.json','rb'))
    list_word = []
    for word_token in word_token:
        if word == word_token[:len(word)]:
            list_word.append(word_token)
        
        if len(list_word) >= 4: # 4 option
            break
    return list_word