from src.Text_Summarizer.logging import logger
from src.Text_Summarizer.pipeline.stage_data_ingestion_pipe import DataIngestionPipeline
from src.Text_Summarizer.pipeline.stage_data_transfromation import DataTransformationPipeline
from src.Text_Summarizer.pipeline.stage_model_training import ModelTrainerPipeline
from src.Text_Summarizer.pipeline.stage_model_evaluation import ModelEvaluationPipeline

STAGE_NAME ="DATA INGESTION STAGE"
STAGE_NAME_T = "DATA TRANSFORMATION STAGE"
STAGE_NAME_MT = "MODEL TRAINING STAGE"
STAGE_NAME_ME = "MODEL EVALUATION"

try:
    logger.info(f'{STAGE_NAME} has initiated')
    initate_data_ingestion = DataIngestionPipeline.initiate_data_ingestion()
    logger.info(f'{STAGE_NAME} has completed')
    logger.info('<----------------------------------->')
    logger.info(f'{STAGE_NAME_T} has initiated')
    initiate_data_transformation=DataTransformationPipeline.initiate_data_transformation()
    logger.info(f'{STAGE_NAME_T} has completed')
    logger.info('<----------------------------------->')
    # logger.info(f'{STAGE_NAME_MT} has initiated')
    # initiate_model_training=ModelTrainerPipeline.initiate_train()
    # logger.info(f'{STAGE_NAME_MT} has completed')
    logger.info('<----------------------------------->')
    logger.info(f'{STAGE_NAME_MT} has initiated')
    initiate_model_evaluation=ModelEvaluationPipeline.evaluate_model()
    logger.info(f'{STAGE_NAME_MT} has completed')
    
except Exception as e:
    logger.exception(e)
    raise e
    
# logger.info("Logger is implemented")