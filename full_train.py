import os
import sys
import logging
from github import context
from datetime import datetime
from dataclasses import dataclass
import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

import numpy as np 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#

@dataclass # @dataclasses we use when we need to store only variables , it saves time & space as we no need to write constructor
class DataIngestionConfig: #any input we require will be given thorugh this class
    train_data_path: str=os.path.join('$GITHUB_WORKSPACE/artifacts',"train.csv")   # artifact is a folder which is used to store these csv
    test_data_path: str=os.path.join('$GITHUB_WORKSPACE/artifacts',"test.csv")
    raw_data_path: str=os.path.join('$GITHUB_WORKSPACE/artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook/data/stud.csv')        # need to change dataset path 
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

# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#

# Any path or input required are initialized here
@dataclass  # @dataclasses we use when we need to store only variables , it saves time & space as we no need to write constructor
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('$GITHUB_WORKSPACE/artifacts',"proprocessor.pkl")

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


# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#


@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("$GITHUB_WORKSPACE/artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()


    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],     # remove last column and feed remaining in X_train
                train_array[:,-1],      # take last column and feed to y_train
                test_array[:,:-1],      # remove last column and feed remaining in X_test
                test_array[:,-1]        # take last column and feed to y_test
            )
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }
            params={
                "Decision Tree": {
                    'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'splitter':['best','random'],
                    # 'max_features':['sqrt','log2'],
                },
                "Random Forest":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                 
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Gradient Boosting":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "Linear Regression":{},
                "XGBRegressor":{
                    'learning_rate':[.1,.01,.05,.001],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "CatBoosting Regressor":{
                    'depth': [6,8,10],
                    'learning_rate': [0.01, 0.05, 0.1],
                    'iterations': [30, 50, 100]
                },
                "AdaBoost Regressor":{
                    'learning_rate':[.1,.01,0.5,.001],
                    # 'loss':['linear','square','exponential'],
                    'n_estimators': [8,16,32,64,128,256]
                }
            }

            # evaluate_model function is in utils file
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models,param=params)
            
            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,    # path for pickle file
                obj=best_model      # create the pickle file from the best model
            )

            predicted=best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)
            return r2_square
            

        except Exception as e:
            raise CustomException(e,sys)

# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#


def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]    # for each model
            para=param[list(models.keys())[i]]  # for each parameter in the model

            # Apply gird search cross-validation for given model and parameter
            gs = GridSearchCV(model,para,cv=3)  
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)


# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)

# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))
    

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) 
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------#

if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))