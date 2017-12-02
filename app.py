# coding=utf-8
from flask import Flask,render_template,request, redirect
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
        
        #softmax = load_model('ULTIMO_MODELLO_V3.h5')
        #softmax.load_weights('ULTIMO_MODELLO_V3_pesi.h5')
        
        #prendiamo da utente
        app.a = request.form['class_obj']
        app.b = request.form['num_vid'] #per ora c'è solo un video
        app.c = request.form['num_frame'] #qesto ci interessa
        
        #decoding
        a = app.a.decode('ascii','ignore').lower() #stringa
        b = app.b
        c = app.c
        
        bor_path = 'data/data_bor/'
        duf_path = 'data/data_duf/'
        ther_path = 'data/data_ther/'
        
        n_video = int(b)  #es = 1
        temp = float(c)
        minuti = int(temp)
        secondi = (temp-minuti) * 100
        t = int((minuti * 60) + secondi)
        
        if a[0:3] =='bor':
            dest_path = bor_path + 'bor_' + str(n_video) + '.pkd'
        elif a[0:3] == 'duf':
            dest_path = duf_path + 'duf_' + str(n_video) + '.pkd'
        elif a[0:3] == 'the':
            dest_path = ther_path + 'ther_'+ str(n_video) + '.pkd'

        nuovo_diz = dill.load(open(dest_path, 'r'))
        
        ritorno = nuovo_diz[t]
        return render_template('index.html', val = ritorno)



@app.route('/primo_video',methods=['GET','POST'])
def next_gabri_1():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('primo_video.html', num = '')
    else:
        # method = POST
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        if a != '':
            temp = float(a)
            minuti = int(temp)
            secondi = (temp-minuti) * 100
            t = int((minuti * 60) + secondi)
            nuovo_diz = dill.load(open('data/data_duf/duf_2.pkd' ,'r'))
            ritorno = nuovo_diz[t]
        else:
            ritorno =  'insert something'
        return render_template('primo_video.html', num = ritorno)

@app.route('/secondo_video',methods=['GET','POST'])
def next_gabri_2():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('secondo_video.html', num = '')
    else:
        # method = POST
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        if a != '':
            temp = float(a)
            minuti = int(temp)
            secondi = (temp-minuti) * 100
            t = int((minuti * 60) + secondi)
            nuovo_diz = dill.load(open('data/data_ther/ther_4.pkd' ,'r'))
            ritorno = nuovo_diz[t]
        else:
            ritorno =  'insert something'
        return render_template('secondo_video.html', num = ritorno)

@app.route('/terzo_video',methods=['GET','POST'])
def next_gabri_3():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('terzo_video.html', num = '')
    else:
        # method = POST
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        if a != '':
            temp = float(a)
            minuti = int(temp)
            secondi = (temp-minuti) * 100
            t = int((minuti * 60) + secondi)
            nuovo_diz = dill.load(open('data/data_bor/bor_2.pkd' ,'r'))
            ritorno = nuovo_diz[t]
        else:
            ritorno =  'insert something'
        return render_template('terzo_video.html', num = ritorno)


@app.route('/quarto_video',methods=['GET','POST'])
def next_gabri_4():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('quarto_video.html', num = '')
    else:
        # method = POST
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        if a != '':
            temp = float(a)
            minuti = int(temp)
            secondi = (temp-minuti) * 100
            t = int((minuti * 60) + secondi)
            nuovo_diz = dill.load(open('data/data_bor/bor_13.pkd' ,'r'))
            ritorno = nuovo_diz[t]
        else:
            ritorno =  'insert something'
        return render_template('quarto_video.html', num = ritorno)



if __name__ == "__main__":
    app.run(debug=True) #,port = int(os.environ.get("PORT", 5000)) ,  host='0.0.0.0', port=port

