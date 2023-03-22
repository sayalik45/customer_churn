from flask import Flask,render_template,request 
from utils import churn_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_data',methods = ['POST','GET'])
def get_data():
    data = request.form

    class_obj = churn_prediction(data)
    result = class_obj.customer_churn()
    # return render_template('index.html',prediction =result )

    if result == 1:
         return render_template('index.html',prediction ="He/she is your customer." )
    if result == 0 :
        return render_template('index.html',prediction ="Sorry he/ she is not your customer anymore." )

    
   
if __name__ == "__main__":
    app.run(host = '0.0.0.0')
    