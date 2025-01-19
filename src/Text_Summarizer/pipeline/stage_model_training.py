from src.Text_Summarizer.config.configuration import ConfigurationManagerMT
from src.Text_Summarizer.components.model_trainer1 import ModelTrainer

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def initiate_train():
        config = ConfigurationManagerMT()
        model_Trainer_Config = config.get_model_trainer_config()
        model_train = ModelTrainer(config=model_Trainer_Config)
        model_train.train1()
        
        
        



