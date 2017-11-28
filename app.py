from flask import Flask,render_template,request
import keras
from keras.models import load_model
import numpy as np
import cv2
from PIL import Image
import os
import dill

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])


def index():
    if request.method == 'POST':
        #my_ris = []
        #softmax = load_model('ULTIMO_MODELLO_V3.h5')
        #softmax.load_weights('ULTIMO_MODELLO_V3_pesi.h5')
        #my_path = os.getcwd()
        #file_list = [el for el in os.listdir(my_path + '/data/bor_1/') if el[0:5] == 'frame']
        #for element in file_list:
        #    img = cv2.imread(my_path + '/data/bor_1/' + element)
        #    resized = cv2.resize(img, (256, 256))
        #    resized_2 = resized.reshape((1,) + resized.shape)
        #    ris = softmax.predict(resized_2)
        #    my_ris.append(ris)
        nuovo_diz = dill.load(open('primo_dizionario.pkd', 'r'))
        ritorno = nuovo_diz
        return render_template('index.html', val = ritorno)
    else:
        #request.method == 'GET':
        return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True) #,port = int(os.environ.get("PORT", 5000)) ,  host='0.0.0.0', port=port

