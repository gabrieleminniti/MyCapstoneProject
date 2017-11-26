from flask import Flask,render_template,request
import keras
from keras.models import load_model
import numpy as np
from PIL import Image
#import pyscreenshot as prendistacazzodiimmagine
import cv2
import os
import PIL
import pyscreenshot

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        screen =pyscreenshot.screenshot()
        half_the_width = screen.size[0] / 2
        half_the_height = screen.size[1] / 2
        img4 = screen.crop(
              (half_the_width - 790,
                half_the_height - 450,
                half_the_width + 790,
                half_the_height + 450)
                )
        img_loaded = np.array(img4)
        resized = cv2.resize(img_loaded, (256, 256))
        blue = resized[:,:,0]
        green = resized[:, :, 1]
        red = resized[:, : , 2]
        immagine_2 = cv2.merge((blue, green, red))
        x = immagine_2.reshape((1, ) + immagine_2.shape)
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        softmax.load_weights('ULTIMO_MODELLO_V3_pesi.h5')
        previsione = softmax.predict(x)
        if previsione[0,0] > .3:
            risultato =  'si tratta di: Borealis '
        elif previsione[0,1] >.3:
            ritultato =  'si tratta di Duffel '
        elif previsione[0,2] > .3:
           risultato ='si tratta di: Thermoball '
        return render_template('index.html', val = risultato)
    else:
        #request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    app.run(debug=True) #, host='0.0.0.0', port=port
