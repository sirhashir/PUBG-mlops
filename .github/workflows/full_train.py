#used to read the data source from a particular dataset
#first localdataset

import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


#there should be some inputs that are required by data ingestion component
#where to save the test data
#where to save the train data

@dataclass # @dataclasses we use when we need to store only variables , it saves time & space as we no need to write constructor
class DataIngestionConfig: #any input we require will be given thorugh this class
    train_data_path: str=os.path.join('artifacts',"train.csv")   # artifact is a folder which is used to store these csv
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

# Through this method we will read the raw data and create a folder as defined in DataIngestionConfig class
# Next inject the train and test data into the folder paths defined in DataIngestionConfig class
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')        # need to change dataset path 
            logging.info('Read the dataset as dataframe')

            # we are creating artifact folder here as this
            # folder contains csv data defined in above method
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)  

            df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            # After train test split save the csv to paths defined above
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of data completed")

            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))