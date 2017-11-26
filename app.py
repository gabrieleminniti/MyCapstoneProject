from flask import Flask,render_template,request
import keras
from keras.models import load_model
import numpy as np
import cv2


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])


def index():
    if request.method == 'POST':
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        cap = cv2.VideoCapture('base_camp.mp4')
        count = 0
        my_list = []
        while count <10:
            ret, frame = cap.read()
            my_list.append( frame)
            count += 1
        my_try = []
        for el in my_list:
            uno =  cv2.resize(el, (256, 256))
            due = uno.reshape((1,) + uno.shape)
            prev = softmax.predict(due)
            if prev[0,0] > .3:
                my_try.append('borealis')
            elif prev[0,1] >.3:
                my_try.append('duffel')
            elif prev[0,2] > .3:
                    my_try.append('thermoball')
        return render_template('index.html', val = my_try)
    else:
        #request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True) #,port = int(os.environ.get("PORT", 5000)) ,  host='0.0.0.0', port=port

