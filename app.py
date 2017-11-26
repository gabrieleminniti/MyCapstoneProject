from flask import Flask,render_template,request
import keras
from keras.models import load_model
import numpy as np
import cv2
from PIL import ImageGrab

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])


def index():
    if request.method == 'POST':
        softmax = load_model('ULTIMO_MODELLO_V3.h5')
        #img = ImageGrab.grab()
        ritorno = 7
        return render_template('index.html', val = ritorno)
    else:
        #request.method == 'GET':
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True) #,port = int(os.environ.get("PORT", 5000)) ,  host='0.0.0.0', port=port

