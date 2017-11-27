from flask import Flask,render_template,request
import keras
from keras.models import load_model
import pyscreenshot as ImageGrab
import numpy as np
import cv2
from PIL import Image


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])


def index():
    if request.method == 'POST':
        im=ImageGrab.grab()
        im.save('screenshot.png')
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        #img = ImageGrab.grab()
        img = cv2.imread('screenshot.png',3)
        resized = cv2.resize(img, (256, 256))
        resized_2 = resized.reshape((1,) + resized.shape)
        ris = softmax.predict(resized_2)
        ritorno = im.size
        return render_template('index.html', val = ritorno)
    else:
        #request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True) #,port = int(os.environ.get("PORT", 5000)) ,  host='0.0.0.0', port=port

