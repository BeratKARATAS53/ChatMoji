from flask import Flask, Blueprint
from flask_cors import CORS
from flask import request, jsonify, make_response
from flask import render_template
import requests

import os
import sys
from io import StringIO

import tensorflow as tf
import pdb
import pickle
import pandas as pd
import numpy as np
import random

from pathlib import Path
from keras.preprocessing.sequence import pad_sequences

from emotion.pythonFiles import emotionModel
from emotion.pythonFiles import testEmotionFlask
from emotion.nlp import preprocess


app = Flask(__name__)
CORS(app)


emoji_list = {
    "fear": ["\ud83d\ude28", "\ud83d\ude31"],
    "joy": ["\ud83d\ude02", "\ud83d\ude39", "\ud83d\udd79\ufe0f"],
    "sadness": ["\ud83d\ude25"],
    "anger": ["\ud83d\udca2", "\ud83d\uddef\ufe0f", "\ud83c\udf4a"]
}

@app.route('/')
def home():
    return 'Done', 201


# @app.route('/predict', methods=['POST'])
# def predict():
#     sentence = request.get_json()
#     print(sentence)
#     if("love" in sentence['sentence']):
#         sentence["sentence"] = "\U0001F496"
#     elif("enjoy" in sentence['sentence']):
#         sentence["sentence"] = "\U0001F923"
#     elif("kill" in sentence['sentence']):
#         sentence["sentence"] = "\U0001F52A"
#     else:
#         sentence["sentence"] = "\U0001F914"
#     return jsonify(sentence)


@app.route('/predictModel', methods=['POST'])
def predictModel():
    sentence = request.get_json()
    result = testEmotionFlask.flask_main(sentence["sentence"])

    maximum = max(result, key=result.get)

    print(result)

    if(maximum == "fear"):
        sentence["sentence"] = "\U0001F628"
    elif(maximum == "anger"):
        sentence["sentence"] = "\U0001F624"
    elif(maximum == "joy"):
        sentence["sentence"] = "\U0001F600"
    else:
        sentence["sentence"] = "\U0001F622"

    return jsonify(sentence)


if __name__ == '__main__':
    app.run(debug=True)
