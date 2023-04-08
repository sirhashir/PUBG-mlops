import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

# Any path or input required are initialized here
@dataclass  # @dataclasses we use when we need to store only variables , it saves time & space as we no need to write constructor
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            
            # Create a numerical processing pipeline
            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),   # handle missing values with median
                ("scaler",StandardScaler())                     # Standardization

                ]
            )

            # Create a categorical pipeline
            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),    # handle missing with frequency 
                ("one_hot_encoder",OneHotEncoder()),                    # One hot encoding
                ("scaler",StandardScaler(with_mean=False))              # Standardization
                ]

            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)
                # our_name      # pipeline    # column
                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    # Datatransformation will actually happen here
    def initiate_data_transformation(self,train_path,test_path):

        try:
            # Read train test files
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            # We want to save this object as pickel (done in save block)
            preprocessing_obj=self.get_data_transformer_object()    # getting objects/methods under this class

            target_column_name="math_score"                         # target column name
            numerical_columns = ["writing_score", "reading_score"]  # numerical columns names

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)   # drop the column which we want to predict
            target_feature_train_df=train_df[target_column_name]                        

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            # This save is defined in utils 
            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,   # path for file 
                obj=preprocessing_obj   # actual file/object to save 

            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)