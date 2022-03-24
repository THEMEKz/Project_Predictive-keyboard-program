import pickle
import heapq
from keras_preprocessing.text import Tokenizer
from keras.models import load_model


def next_word(text):
    model = load_model('nextword1.h5')
    tokens = pickle.load('tokenizer1.pkl')

    text_token = tokens.texts_to_sequences([text])
    pred = model.predict(text_token)[0]
    top5_pop = heapq.nlargest(5, range(len(pred)), pred.take)

    func = lambda x : [x]
    decode_seq = tokens.sequences_to_texts(list(map(func,top5_pop)))
    return decode_seq