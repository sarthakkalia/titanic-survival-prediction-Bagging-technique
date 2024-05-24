import pickle
from flask import Flask,request,jsonify,render_template
import pandas as pd
import numpy as np

application = Flask(__name__)
app=application

model = pickle.load(open('models\\baggingTechniques.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        pclass=int(request.form.get("pclass"))
        sex_encoded = int(request.form.get('sex_encoded'))
        age = float(request.form.get('age'))
        fare = float(request.form.get('fare'))
        embarked_encoded = int(request.form.get('embarked_encoded'))
        class_encoded = int(request.form.get('class_encoded'))
        who_encoded = int(request.form.get('who_encoded'))
        deck_encoded = int(request.form.get('deck_encoded'))
        embark_town_encoded = int(request.form.get('embark_town_encoded'))
        alone = int(request.form.get('alone'))

        new_data = [[pclass, sex_encoded, age, fare, embarked_encoded, class_encoded, who_encoded, deck_encoded,embark_town_encoded,alone]]
        predict=model.predict(new_data)
       
        if predict[0] ==1 :
            result = 'Alive'
        else:
            result ='Dead'
            
        return render_template('single_prediction.html',result=result)

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")