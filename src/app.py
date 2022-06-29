from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
from PIL import Image
import base64
import io
from Backend.algorithm import *

app = Flask(__name__,template_folder='Frontend', static_folder='Frontend')
app.secret_key = "secret key"

# GLOBAL VARIABLES
cache = {}
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    #get File dan Rate dari form submission
    file = request.files['file']

    #save image original
    ori_image = Image.open(file)
    img_format = ori_image.format
    data = io.BytesIO()
    ori_image.save(data,img_format)
    encoded_ori_image = base64.b64encode(data.getvalue())
    encoded_image = encoded_ori_image

    cache["format"] = img_format
    cache["base"] = encoded_ori_image
    cache["current"]= encoded_image

    return render_template('index.html', filename=encoded_image.decode('utf-8'), basename = encoded_ori_image.decode('utf-8'), img_format= img_format)

@app.route('/<command>', methods=['POST'])
def edit_image(command):
    encoded_ori_image = cache["base"]
    img_format = cache["format"]
    decoded_data=io.BytesIO(base64.b64decode(cache["current"]))
    
    if command =="turnleft":
        encoded_image = turnleft(decoded_data)
    elif command == "turnright":
        encoded_image = turnright(decoded_data)
    elif command == "fliph":
        encoded_image = fliph(decoded_data)
    elif command == "flipv":
        encoded_image = flipv(decoded_data)
    else: 
        encoded_image = encoded_ori_image

    cache["current"]= encoded_image

    return render_template('index.html', filename=encoded_image.decode('utf-8'), basename = encoded_ori_image.decode('utf-8'), img_format= img_format)

if __name__ == '__main__':
    app.run(debug = True)