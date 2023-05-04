import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application=Flask(__name__)

app=application

CORS(app)

## Route for a home page

# class CustomData:
#     def __init__(self, data):
#         self.assists = data.get('assists')
#         self.boosts = data.get('boosts')
#         self.headshotKills = data.get('headshotKills')
#         self.kills = data.get('kills')
#         self.longestKill = data.get('longestKill')
#         self.matchDuration = data.get('matchDuration')
#         self.revives = data.get('revives')
#         self.teamKills = data.get('teamKills')
#         self.vehicleDestroys = data.get('vehicleDestroys')
#         self.walkDistance = data.get('walkDistance')
#         self.weaponsAcquired = data.get('weaponsAcquired')
#         self.matchType = data.get('matchType')

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint(): 
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=request.get_json()
        data = data.get('Headers')
        data = data.get('data')
        print(data.items())

        data_frame = CustomData(
        assists = data.get('assists'),
        boosts = data.get('boosts'),
        headshotKills = data.get('headshotKills'),
        kills = data.get('kills'),
        longestKill = data.get('longestKill'),
        matchDuration = data.get('matchDuration'),
        revives = data.get('revives'),
        teamKills = data.get('teamKills'),
        vehicleDestroys = data.get('vehicleDestroys'),
        walkDistance = data.get('walkDistance'),
        weaponsAcquired = data.get('weaponsAcquired'),
        matchType = data.get('matchType')
        )

        pred_df=data_frame.get_data_as_data_frame()
        
        print("Before Prediction")

        
        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print( results)
        # return render_template('home.html',results=results[0])
        return str(results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)
