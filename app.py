from flask import Flask,request,render_template
import numpy as np
import pandas as pd


#lsof -i :5000

# COMMAND   PID           USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
# ControlCe 571 dushyantsharma   10u  IPv4 0x81b2725f7240aa54      0t0  TCP *:commplex-main (LISTEN)
# ControlCe 571 dushyantsharma   11u  IPv6 0xb30f9d0b8587c843      0t0  TCP *:commplex-main (LISTEN)
#(venv) ➜  End2End-ML-Deployment-Ops git:(main) ✗ kill -9 571  


# app.run(host="0.0.0.0", port=5001)  -> use different port if the port is busy

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5001)   


