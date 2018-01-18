import pickle
import flask
import time
import json
from TwoLayer import TwoLayerNet
from flask import Flask, g
from flask import jsonify
from flask import request
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

def processing(filepath):
  I5 = Image.open(filepath)
  I5_s = I5.resize((28, 28), Image.ANTIALIAS)
  I5_sa = np.array(I5_s)
  I = rgb2gray(I5_sa)
  if(np.mean(I) > 128):
    return np.argmax(network.predict( 1 - I.reshape(1, 784) / 255))
  else:
    return np.argmax(network.predict( I.reshape(1, 784) / 255))
  


network = pickle.load(open("network.pkl", "rb"))
app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False


@app.route('/model/<fp>', methods=['GET'])
def model(fp):  
    ans = processing(str(fp)+'.png')
    res = jsonify(ans = int(ans))
    res.headers['Content-Type'] = 'application/json; charset=utf-8'
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET'
    res.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return res


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=1234)
