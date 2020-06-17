from flask import Flask, Blueprint
from flask import request, jsonify, make_response
from flask import render_template
from flask_cors import CORS
import requests

import os
import sys

import numpy as np
from random import randint

from emotion.pythonFiles import testEmotionFlask


app = Flask(__name__)
CORS(app)


emoji_list = {
    "fear": ["\ud83d\ude28", "\ud83d\ude31","\ud83d\ude30"],
    "joy": ["\ud83d\ude02", "\ud83d\ude39", "\ud83d\ude00"],
    "sadness": ["\ud83d\ude22","\ud83d\ude2d","\ud83d\ude3f"],
    "anger": ["\ud83d\ude20", "\ud83d\udc7f", "\ud83d\ude24"]
}


@app.route('/')
def home():
    return 'Done', 201


@app.route('/predict', methods=['POST'])
def predict():
    sentence = request.get_json()
    result = testEmotionFlask.flask_main(sentence["sentence"])

    maximum = max(result, key=result.get)

    new_result = {key: "%"+str(format(value*100, ".1f"))
                  for key, value in result.items()}

    sentence["result"] = new_result

    rand = randint(0,2)
    sentence["sentence"] = emoji_list[maximum][rand]

    return jsonify(sentence)


if __name__ == '__main__':
    app.run(debug=True)
