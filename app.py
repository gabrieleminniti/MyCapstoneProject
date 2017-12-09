# coding=utf-8
from flask import Flask,render_template,request, redirect
import keras
from keras.models import load_model
import numpy as np
import cv2
from PIL import Image
import os
import dill
import re

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


# video duffel_1 --> durata 4.05
@app.route('/primo_video',methods=['GET','POST'])
def next_gabri_1():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('primo_video.html', num = '')
    else:
        # method = POST
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        match = re.findall(r'\d+', a)
        if match != []:
            minuti = int(match[0]) #minuti
            if minuti >= 5:
                ritorno = 'the video is about four minutes'
            else:
                secondi = int(match[1]) #secondi
                if secondi >59:
                    ritorno = 'a minute has maximum 59 seconds'
                else:
                    idx = (minuti * 60) + secondi
                    if idx >= 246:
                        ritorno = 'insert a valid moment'
                    else:
                        nuovo_diz = dill.load(open('data/data_duf/duf_2.pkd' ,'r'))
                        ritorno = nuovo_diz[idx]
        else:
            ritorno = 'you fail to insert the moment that you wanna recognize'
    return render_template('primo_video.html', num = ritorno)

#video thermoball_1 --> 2.33
@app.route('/secondo_video',methods=['GET','POST'])
def next_gabri_2():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('secondo_video.html', num = '')
    else:
        # method = POST
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        match = re.findall(r'\d+', a)
        if match != []:
            minuti = int(match[0]) #minuti
            if minuti >= 3:
                ritorno = 'the video is about two minutes'
            else:
                secondi = int(match[1]) #secondi
                if secondi >59:
                    ritorno = 'a minute has maximum 59 seconds'
                else:
                    idx = (minuti * 60) + secondi
                    if idx >= 153:
                        ritorno = 'insert a valid moment'
                    else:
                        nuovo_diz = dill.load(open('data/data_ther/ther_4.pkd' ,'r'))
                        ritorno = nuovo_diz[idx]
        else:
            ritorno = 'you fail to insert the moment that you wanna recognize'
    return render_template('secondo_video.html', num = ritorno)


#video borealis_1
@app.route('/terzo_video',methods=['GET','POST'])
def next_gabri_3():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('terzo_video.html', num = '')
    else:
        # method = POST
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        match = re.findall(r'\d+', a)
        if match != []:
            minuti = int(match[0]) #minuti
            if minuti >= 5:
                ritorno = 'the video is about four minutes'
            else:
                secondi = int(match[1]) #secondi
                if secondi >59:
                    ritorno = 'a minute has maximum 59 seconds'
                else:
                    idx = (minuti * 60) + secondi
                    if idx >= 274:
                        ritorno = 'insert a valid moment'
                    else:
                        nuovo_diz = dill.load(open('data/data_bor/bor_2.pkd' ,'r'))
                        ritorno = nuovo_diz[idx]
        else:
            ritorno = 'you fail to insert the moment that you wanna recognize'
    return render_template('terzo_video.html', num = ritorno)




#video borealis_2 --> 1.02
@app.route('/quarto_video',methods=['GET','POST'])
def next_gabri_4():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('quarto_video.html', num = '')
    else:
        # method = POST
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        match = re.findall(r'\d+', a)
        if match != []:
            minuti = int(match[0]) #minuti
            if minuti >= 2:
                ritorno = 'the video is about one'
            else:
                secondi = int(match[1]) #secondi
                if secondi >59:
                    ritorno = 'a minute has maximum 59 seconds'
                else:
                    idx = (minuti * 60) + secondi
                    if idx >= 63:
                        ritorno = 'insert a valid moment'
                    else:
                        nuovo_diz = dill.load(open('data/data_bor/bor_13.pkd' ,'r'))
                        ritorno = nuovo_diz[idx]
        else:
            ritorno = 'you fail to insert the moment that you wanna recognize'
    return render_template('quarto_video.html', num = ritorno)


#video duffel_2 --> 1.17
@app.route('/quinto_video',methods=['GET','POST'])
def next_gabri_5():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('quinto_video.html', num = '')
    else:
        # method = POST
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        match = re.findall(r'\d+', a)
        if match != []:
            minuti = int(match[0]) #minuti
            if minuti >= 2:
                ritorno = 'the video is about one minute'
            else:
                secondi = int(match[1]) #secondi
                if secondi >59:
                    ritorno = 'a minute has maximum 59 seconds'
                else:
                    idx = (minuti * 60) + secondi
                    if idx >= 77:
                        ritorno = 'insert a valid moment'
                    else:
                        nuovo_diz = dill.load(open('data/data_duf/duf_3.pkd' ,'r'))
                        ritorno = nuovo_diz[idx]
        else:
            ritorno = 'you fail to insert the moment that you wanna recognize'
    return render_template('quinto_video.html', num = ritorno)


#video thermoball_2
@app.route('/sesto_video',methods=['GET','POST'])
def next_gabri_6():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('sesto_video.html', num = '')
    else:
        # method = POST
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        match = re.findall(r'\d+', a)
        if match != []:
            minuti = int(match[0]) #minuti
            if minuti >= 3:
                ritorno = 'the video is about two minutes'
            else:
                secondi = int(match[1]) #secondi
                if secondi >59:
                    ritorno = 'a minute has maximum 59 seconds'
                else:
                    idx = (minuti * 60) + secondi
                    if idx >= 121:
                        ritorno = 'insert a valid moment'
                    else:
                        nuovo_diz = dill.load(open('data/data_ther/ther_5.pkd' ,'r'))
                        ritorno = nuovo_diz[idx]
        else:
            ritorno = 'you fail to insert the moment that you wanna recognize'
    return render_template('sesto_video.html', num = ritorno)



#video thermoball_3  --> 2.36
@app.route('/settimo_video',methods=['GET','POST'])
def next_gabri_7():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('settimo_video.html', num = '')
    else:
        # method = POST
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        match = re.findall(r'\d+', a)
        if match != []:
            minuti = int(match[0]) #minuti
            if minuti >= 3:
                ritorno = 'the video is about two minutes'
            else:
                secondi = int(match[1]) #secondi
                if secondi >59:
                    ritorno = 'a minute has maximum 59 seconds'
                else:
                    idx = (minuti * 60) + secondi
                    if idx >= 156:
                        ritorno = 'insert a valid moment'
                    else:
                        nuovo_diz = dill.load(open('data/data_ther/daai.pkd' ,'r'))
                        ritorno = nuovo_diz[idx]
        else:
            ritorno = 'you fail to insert the moment that you wanna recognize'
    return render_template('settimo_video.html', num = ritorno)


#video borealis_3 --> 3.41
@app.route('/ottavo_video',methods=['GET','POST'])
def next_gabri_8():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('ottavo_video.html', num = '')
    else:
        # method = POST
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        match = re.findall(r'\d+', a)
        if match != []:
            minuti = int(match[0]) #minuti
            if minuti >= 4:
                ritorno = 'the video is about three minutes'
            else:
                secondi = int(match[1]) #secondi
                if secondi >59:
                    ritorno = 'a minute has maximum 59 seconds'
                else:
                    idx = (minuti * 60) + secondi
                    if idx >= 222:
                        ritorno = 'insert a valid moment'
                    else:
                        nuovo_diz = dill.load(open('data/data_bor/bor_3.pkd' ,'r'))
                        ritorno = nuovo_diz[idx]
        else:
            ritorno = 'you fail to insert the moment that you wanna recognize'
    return render_template('ottavo_video.html', num = ritorno)



#video duffel_3
@app.route('/nono_video',methods=['GET','POST'])
def next_gabri_9():#can't have two functions with the same name
    if request.method == 'GET':
        return render_template('nono_video.html', num = '')
    else:
        # method = POST
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        app.a = request.form['sec']
        a = app.a.encode('ascii','ignore').lower()
        match = re.findall(r'\d+', a)
        if match != []:
            minuti = int(match[0]) #minuti
            if minuti >= 9:
                ritorno = 'the video is about eight minutes'
            else:
                secondi = int(match[1]) #secondi
                if secondi >59:
                    ritorno = 'a minute has maximum 59 seconds'
                else:
                    idx = (minuti * 60) + secondi
                    if idx >= 522:
                        ritorno = 'insert a valid moment'
                    else:
                        nuovo_diz = dill.load(open('data/data_duf/duf_4.pkd' ,'r'))
                        ritorno = nuovo_diz[idx]
        else:
            ritorno = 'you fail to insert the moment that you wanna recognize'
    return render_template('nono_video.html', num = ritorno)


@app.route('/info', methods = ['GET', 'POST'])
def info():
    if request.method == 'GET':
        return render_template('info.html')
    else:
        return render_template('info.html')

if __name__ == "__main__":
    app.run(debug=True) #,port = int(os.environ.get("PORT", 5000)) ,  host='0.0.0.0', port=port

