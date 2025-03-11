from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import os  # Import os for setting the port

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)  # This is the correct WSGI application instance
app = application  # Ensure compatibility with Elastic Beanstalk v2env (#port =  5001   #http://127.0.0.1:5001/predictdata or http://localhost:5001/predictdata ( IP address for localhost - 127.0.0.1))

## Route for a home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("After Prediction")
        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Elastic Beanstalk uses port 8000
    app.run(host="0.0.0.0", port=port)