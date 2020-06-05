from flask import Flask
from flask_cors import CORS
from flask import request
from flask import jsonify
from flask import render_template
from flask import Blueprint

import os
import sys
import tensorflow as tf
import pdb
import pickle
import pandas as pd
import numpy as np

from pathlib import Path
from keras.preprocessing.sequence import pad_sequences

from emotion.pythonFiles import emotionModel
from emotion.pythonFiles import preprocess


app = Flask(__name__)
CORS(app)


def get_test_data():
    data_path = Path('../test.csv').resolve()
    data = pd.read_csv(data_path, header=None, names=['text'])
    return data

def get_encoder():
    encoder_path = Path('./models/emotion_recognition/encoder.pickle').resolve()
    with encoder_path.open('rb') as file:
        encoder = pickle.load(file)
    return encoder

def preprocess_data():
    cleaned_data = preprocess(data.text)
    sequences = [text.split() for text in cleaned_data]
    list_tokenized = tokenizer.texts_to_sequences(sequences)
    x_data = pad_sequences(list_tokenized, maxlen=100)
    return x_data

def predict():
    x_data = preprocess_data()
    y_pred = model.predict(x_data)
    for index, value in enumerate(np.sum(y_pred, axis=0) / len(y_pred)):
        print(encoder.classes_[index] + ": " + str(value))
    y_pred_argmax = y_pred.argmax(axis=1)
    data_len = len(y_pred_argmax)
    for index, value in enumerate(np.unique(y_pred_argmax)):
        print(encoder.classes_[index] + ": " + str(len(y_pred_argmax[y_pred_argmax == value]) / data_len))


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
    x_data = preprocess_data()
    y_pred = model.predict(x_data)
    for index, value in enumerate(np.sum(y_pred, axis=0) / len(y_pred)):
        print(encoder.classes_[index] + ": " + str(value))
    y_pred_argmax = y_pred.argmax(axis=1)
    data_len = len(y_pred_argmax)
    for index, value in enumerate(np.unique(y_pred_argmax)):
        print(encoder.classes_[index] + ": " + str(len(y_pred_argmax[y_pred_argmax == value]) / data_len))


if __name__ == '__main__':
    tokenizer_path = Path('../datasets/tokenizer.pickle').resolve()
    with tokenizer_path.open('rb') as file:
        tokenizer = pickle.load(file)

    input_length = 100
    model = emotionModel.emotionModel(tokenizer, input_length)
    model_weights_path = Path('../models/emotion_recognition/model_weights.h5').resolve()
    model.load_weights(model_weights_path.as_posix())

    data = get_test_data()
    encoder = get_encoder()
    predict()
    app.run(debug=True)
