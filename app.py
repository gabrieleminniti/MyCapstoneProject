# coding=utf-8
from flask import Flask,render_template,request
import keras
from keras.models import load_model
import numpy as np
import cv2
from PIL import Image
import os
import dill

app = Flask(__name__)

app.a = 0
app.b = 0
app.c = 0


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        #request.method == 'POST':
        
        ## per far passare un po di tempo facciamo caricare il modello nonostante non lo utilizzeremo
        
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        softmax.load_weights('ULTIMO_MODELLO_V3_pesi.h5')
        
        #prendiamo da utente
        app.a = request.form['class_obj']
        app.b = request.form['num_vid'] #per ora c'è solo un video
        app.cc = request.form['num_frame'] #qesto ci interessa
        
        #encoding
        a = app.a.decode('ascii','ignore').lower() #stringa
        b = app.b.decode('ascii', 'ignore')
        c = app.c.decode('ascii', 'ignore')
        
        bor_path = '/data/data_bor/'
        duf_path = '/data/data_bor/'
        ther_path = '/data/data_bor/'
        
        n_video = int(b)  #es = 1
        n_frame = int(c)
        
        if a[0:3] =='bor':
            open_data = 'bor_' , n_video
        elif a[0:3] == 'duf':
            open_data = 'duf_' , n_video
        elif a[0:3] == 'the':
            open_data = 'ther_', n_video

        nuovo_diz = dill.load(open(bor_path + open_data, 'r'))
        
        ritorno = nuovo_diz[n_frame]
        return render_template('index.html', val = ritorno)







if __name__ == "__main__":
    app.run(debug=True) #,port = int(os.environ.get("PORT", 5000)) ,  host='0.0.0.0', port=port

