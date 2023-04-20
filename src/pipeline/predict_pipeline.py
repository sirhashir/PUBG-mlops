import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path = "artifacts/proprocessor.pkl"

            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        assists: int,
        boosts: int,
        headshotKills: int,
        kills: int,
        longestKill: int,
        matchDuration: int,
        revives: int,
        teamKills: int,
        vehicleDestroys: int,
        walkDistance: int,
        weaponsAcquired: int,
        
        matchType: str,
        ):

        self.assists = assists
        self.boosts = boosts
        self.headshotKills = headshotKills
        self.kills = kills
        self.longestKill = longestKill
        self.matchDuration = matchDuration
        self.revives = revives
        self.teamKills = teamKills
        self.vehicleDestroys = vehicleDestroys
        self.walkDistance = walkDistance
        self.weaponsAcquired = weaponsAcquired
        self.matchType = matchType



    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "assists": [self.assists],
                "boosts": [self.boosts],
                "headshotKills": [self.headshotKills],
                "kills": [self.kills],
                "longestKill": [self.longestKill],
                "matchDuration": [self.matchDuration],
                "revives": [self.revives],
                "teamKills": [self.teamKills],
                "vehicleDestroys": [self.vehicleDestroys],
                "walkDistance": [self.walkDistance],
                "weaponsAcquired": [self.weaponsAcquired],
                "matchType": [self.matchType],

            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)