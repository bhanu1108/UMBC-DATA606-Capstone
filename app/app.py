from flask import Flask, render_template, request, jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
with open('Autos_Final_model.pkl', 'rb') as fp:
    model = pickle.load(fp)
    print("loaded successfull")
@app.route('/',methods=['GET'])

def Home():
    return render_template('index.html')

standard_to = StandardScaler()

@app.route("/predict", methods=['POST'])

def predict():
    
    if request.method == 'POST':

        Year = int(request.form['Year'])
        monthreg=float(request.form['monthreg'])
        Kms_Driven=int(request.form['Kms_Driven'])
        # Kms_Driven2=np.log(Kms_Driven)
        GearBox=int(request.form['GearBox'])
        PowerPS=int(request.form['PowerPS'])
        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if Fuel_Type_Petrol=='Benzin':
            Fuel_Type_Petrol=0
        elif Fuel_Type_Petrol=='LPG':
            Fuel_Type_Petrol=2
        else:
            Fuel_Type_Petrol=1
        
        

        Brand=int(request.form['brand'])
        print("OK")
        print(Year,GearBox,PowerPS,Kms_Driven,monthreg,Fuel_Type_Petrol,Brand)
        prediction=model.predict([[Year,GearBox,PowerPS,Kms_Driven,monthreg,Fuel_Type_Petrol,Brand]])
        print(prediction)
        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="✅ Selling Price of the Car is {} 👍".format(output))

    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
