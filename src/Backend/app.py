from flask import Flask, flash, request, redirect, url_for, render_template,jsonify
from flask_cors import CORS
import urllib.request
import os
from werkzeug.utils import secure_filename
from PIL import Image
import base64
import io
from milestone1 import *
from milestone2 import *
from milestone3 import *
import re

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST','GET'])
def home():
    return jsonify({"status": "success", "message": "Welcome to the API"})

@app.route('/<command>', methods=['POST','GET'])
def edit_image(command):
    decoded_data = request.get_json()

    decoded_data = re.sub('^data:image/.+;base64,', '', decoded_data["imgsource"])
    decoded_data = io.BytesIO(base64.b64decode(decoded_data))

    if command =="turnleft":
        encoded_image = turnleft(decoded_data)
    elif command == "turnright":
        encoded_image = turnright(decoded_data)
    elif command == "fliph":
        encoded_image = fliph(decoded_data)
    elif command == "flipv":
        encoded_image = flipv(decoded_data)
    elif command == "greyscale":
        encoded_image = greyscale(decoded_data)
    elif command == "negative":
        encoded_image = negative(decoded_data)
    elif command == "complement":
        encoded_image = complement(decoded_data)
    elif command == "zoomin":
        encoded_image = zoomin(decoded_data)
    elif command == "zoomout":
        encoded_image = zoomout(decoded_data)
    elif command == "brighten":
        encoded_image = brighten(75,decoded_data)
    elif command == "darken":
        encoded_image = brighten(-75,decoded_data)
    elif command == "contrast":
        encoded_image = contrast(decoded_data)
    elif command == "tpangkat":
        encoded_image = transformasi("pangkat",decoded_data)
    elif command == "tlog":
        encoded_image = transformasi("logaritma",decoded_data)
    elif command == "gblur":
        encoded_image = gauss("blur",decoded_data)
    elif command == "hfilter":
        encoded_image = gauss("sharpen",decoded_data)
    elif command == "lfilter":
        encoded_image = gauss("smooth",decoded_data)
    else: 
        encoded_image = None

    return jsonify({"result": encoded_image.decode('utf-8')})


if __name__ == '__main__':
    app.run(debug = True)