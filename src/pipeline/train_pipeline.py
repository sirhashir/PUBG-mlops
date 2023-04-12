import sys
sys.path.append('C:/Users/Asus/Desktop/GitHub-Action')


from src.components import data_ingestion, data_transformation, model_trainer

# Create an instance of the DataIngestion class
di = data_ingestion.DataIngestion()

# Create an instance of the DataTransformation class
dt = data_transformation.DataTransformation()

# Create an instance of the ModelTrainer class
mt = model_trainer.ModelTrainer()

train_path,test_path = di.initiate_data_ingestion()
train_arr,test_arr,_ = dt.initiate_data_transformation(train_path, test_path)
mt.initiate_model_trainer(train_arr, test_arr)