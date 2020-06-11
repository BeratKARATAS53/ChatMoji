from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request, jsonify, make_response
from flask import render_template

import os
import sys
from io import StringIO
    
import tensorflow as tf
import pdb
import pickle
import pandas as pd
import numpy as np

from pathlib import Path
from keras.preprocessing.sequence import pad_sequences

from emotion.pythonFiles import emotionModel
from emotion.nlp import preprocess


app = Flask(__name__)
CORS(app)

tokenizer_path = Path('./emotion/datasets/sentiment_analysis/tokenizer.pickle').resolve()
with tokenizer_path.open('rb') as file:
    tokenizer = pickle.load(file)
    
def get_test_data():
    data_path = Path('./emotion/test.csv').resolve()
    data = pd.read_csv(data_path, header=None, names=['text'])
    return data

def string_to_pandas(sentence):
    three = "\"\"\""
    sentence = three + sentence + three
    data = StringIO(sentence)
    df = pd.read_csv(data, header=None, names=['text'])
    return df

def get_encoder():
    encoder_path = Path('./emotion/models/emotion_recognition/encoder.pickle').resolve()
    with encoder_path.open('rb') as file:
        encoder = pickle.load(file)
    return encoder

def preprocess_data(sentence):
    sentence = string_to_pandas(sentence)
    cleaned_data = preprocess(sentence.text)
    sequences = [text.split() for text in cleaned_data]
    list_tokenized = tokenizer.texts_to_sequences(sequences)
    x_data = pad_sequences(list_tokenized, maxlen=100)
    return x_data

def predictEmotion(sentence):
    input_length = 100
    model = emotionModel.emotionModel(tokenizer, input_length)
    model_weights_path = Path('./emotion/models/emotion_recognition/model_weights.h5').resolve()
    model.load_weights(model_weights_path.as_posix())
    
    x_data = preprocess_data(sentence)
    y_pred = model.predict(x_data)
    
    result = {}
    for index, value in enumerate(np.sum(y_pred, axis=0) / len(y_pred)):
        result[encoder.classes_[index]] =value
    
    return result

@app.route('/')
def home():
    return 'Done', 201


@app.route('/predict', methods=['POST'])
def predict():
    sentence = request.get_json()
    print(sentence)
    if("love" in sentence['sentence']):
        sentence["sentence"] = "\U0001F496"
    elif("enjoy" in sentence['sentence']):
        sentence["sentence"] = "\U0001F923"
    elif("kill" in sentence['sentence']):
        sentence["sentence"] = "\U0001F52A"
    else:
        sentence["sentence"] = "\U0001F914"
    return jsonify(sentence)


@app.route('/predictModel', methods=['POST'])
def predictModel():
    sentence = request.get_json()
    sentence = sentence["sentence"]
    result = predictEmotion(sentence)
    
    maximum = max(result, key=result.get)  # Just use 'min' instead of 'max' for minimum.
    
    print(result)
    return jsonify({"result": maximum})


data = get_test_data()
encoder = get_encoder()

if __name__ == '__main__':
    app.run(debug=True)
