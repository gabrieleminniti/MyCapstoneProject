from flask import Flask,render_template,request
import keras
from keras.models import load_model
import os
import numpy as np
from PIL import ImageGrab, Image
import sklearn
import skimage
from skimage import io
import cv2


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():
    if request.method == 'POST':
        immagine = ImageGrab.grab()
        half_the_width = immagine.size[0] / 2
        half_the_height = immagine.size[1] / 2
        img4 = immagine.crop(
                (half_the_width - 1280,
                half_the_height - 500,
                half_the_width + 440,
                half_the_height + 290)
                )
        img_loaded = np.array(img4)
        resized = cv2.resize(img_loaded, (256, 256))
        blue = resized[:,:,0]
        green = resized[:, :, 1]
        red = resized[:, : , 2]
        immagine = cv2.merge((blue, green, red))
        x = immagine.reshape((1, ) + immagine.shape)
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        softmax.load_weights('ULTIMO_MODELLO_V3_pesi.h5')
        previsione = softmax.predict(x)
        if previsione[0,0] > .3:
            return ' si tratta di: Borealis '
        elif previsione[0,1] >.3:
            return 'si tratta di Duffel '
        elif previsione[0,2] > .3:
            return 'si tratta di: Thermoball '
    else:
        
        #request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
