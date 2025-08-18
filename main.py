from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.exception.exception import NetworkSecurityException
from src.logging.logger import logging
from src.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from src.entity.config_entity import TrainingPipelineConfig

# from networksecurity.components.model_trainer import ModelTrainer
# from networksecurity.entity.config_entity import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
from src.entity.config_entity import ModelTrainerConfig

import sys

if __name__=='__main__':
    try:
        # Data Ingestion phase
        trainingpipelineconfig=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")
        data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(data_ingestion_artifacts)

        # Data Validation phase
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(data_ingestion_artifacts, data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)

        # Data Transformation phase
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        logging.info("Initiate the data transformation")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(data_transformation_artifact)

        # Model Training & Evaluation phase
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config, data_transformation_artifact)
        logging.info("Initiate the model training and evaluation")
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model Training and Evaluation Completed")
        print(model_trainer_artifact)

    except Exception as e:
           raise NetworkSecurityException(e,sys)
