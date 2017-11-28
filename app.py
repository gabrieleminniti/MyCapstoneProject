from flask import Flask,render_template,request
import keras
from keras.models import load_model
import numpy as np
import cv2
from PIL import Image


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])


def index():
    if request.method == 'POST':
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        softmax.load_weights('ULTIMO_MODELLO_V3_pesi.h5')
        img = cv2.imread('data/test.png',3)
        resized = cv2.resize(img, (256, 256))
        resized_2 = resized.reshape((1,) + resized.shape)
        ris = softmax.predict(resized_2)
        if ris[0,0]>.3:
            ritorno = 'borealis'
        elif ris[0,1] > .3:
            ritorno = 'duffel'
        elif ris[0,2] >.3:
            ritorno = 'duffel'
        else:
            ritorno = 'no idea'
        return render_template('index.html', val = ritorno)
    else:
        #request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True) #,port = int(os.environ.get("PORT", 5000)) ,  host='0.0.0.0', port=port

