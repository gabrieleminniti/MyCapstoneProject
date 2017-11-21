from flask import Flask,render_template,request


app_gabri = Flask(__name__)
@app_gabri.route('/index_gabri',methods=['GET','POST'])
def index_gabri():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return ( 'noooooo')



if __name__ == "__main__":
    app_gabri.run(debug=True)
