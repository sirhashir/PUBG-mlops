import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

import logging
from datetime import datetime
import os

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(format="%(asctime)s::%(levelname)s::%(message)s",
                    level=logging.INFO,
                    filename=LOG_FILE_PATH
                    )


# Define the logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Define the file handler and formatter
file_handler = logging.FileHandler(LOG_FILE_PATH)
formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger instance
logger.addHandler(file_handler)


application=Flask(__name__)

app=application

CORS(app)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])


def predict_datapoint(): 
    logger.info("app started")
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=request.get_json()
        data = data.get('Headers')
        data = data.get('data')
        print(data.items())

        # Check if all features are present
        required_features = ['assists', 'boosts', 'headshotKills', 'kills', 'longestKill', 'matchDuration', 'revives', 'teamKills', 'vehicleDestroys', 'walkDistance', 'weaponsAcquired']
        if not all(feature in data for feature in required_features):
            return 'The model requires all input features to make accurate predictions.', 400
        
        # Check if matchType is valid
        valid_match_types = ['solo', 'solo-fpp', 'duo', 'duo-fpp', 'squad', 'squad-fpp', 'normal-squad-fpp', 'flarefpp', 'normal-solo-fpp', 'crashfpp', 'normal-duo-fpp']
        match_type = data.get('matchType')
        if match_type not in valid_match_types:
            return "The provided 'matchType' value is invalid. Allowed values are ['solo', 'solo-fpp', 'duo', 'duo-fpp', 'squad', 'squad-fpp'].", 400


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

        logger.info(assists)
        logger.info(boosts)
        logger.info(headshotKills)
        logger.info(kills)
        logger.info(longestKill)
        logger.info(matchDuration)
        logger.info(revives)
        logger.info(teamKills)
        logger.info(vehicleDestroys)
        logger.info(walkDistance)
        logger.info(weaponsAcquired)
        logger.info(matchType)
        


        pred_df=data_frame.get_data_as_data_frame()
        
        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)
        print(results)
        
        # return render_template('home.html',results=results[0])
        return str(results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)


# ---------------------- END OF CODE ------------------------------