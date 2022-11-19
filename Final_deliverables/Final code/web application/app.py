import numpy as np
from PIL import Image
import os
from flask import Flask, request, render_template, url_for,redirect
from werkzeug.utils import secure_filename, redirect
from gevent.pywsgi import WSGIServer
from keras.models import load_model
import cv2
from keras.preprocessing import image
from tensorflow.keras.preprocessing import image
from flask import send_from_directory

FOLDER ='static/upload'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FOLDER

model = load_model("forest.h5")

@app.route('/')
def index():
    return render_template('HDR front end.html')

@app.route('/Detection', methods=['GET', 'POST'])
def Detection():
    if request.method == 'POST':
        return redirect(url_for('HDR front end.html'))
    return render_template('Detection.html')
