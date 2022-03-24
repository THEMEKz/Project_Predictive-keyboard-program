import pickle
import heapq
from keras_preprocessing.text import Tokenizer
from keras.models import load_model
from numpy import empty


def next_word(text,num_op):
    model = load_model('C:\\Users\\nanth\\Desktop\\Project\\model_nextword\\nextword1.h5')
    tokens = pickle.load(open('C:\\Users\\nanth\\Desktop\\Project\\model_nextword\\tokenizer1.pkl','rb'))

    text_token = tokens.texts_to_sequences([text])
    if len(text_token[0]):
        pred = model.predict(text_token)[0]
        top5_pop = heapq.nlargest(num_op, range(len(pred)), pred.take)

        func = lambda x : [x]
        decode_seq = tokens.sequences_to_texts(list(map(func,top5_pop)))
        return decode_seq
    return []

# print(next_word('word'))