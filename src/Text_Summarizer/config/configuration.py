from src.Text_Summarizer.utils.common import * 
from src.Text_Summarizer.constants import *
from src.Text_Summarizer.entity import DataIngestionConfig ,DataTransformationConfig , ModelTrainerConfig , ModelEvaluationConfig

class ConfigurationManager:
    def __init__(self,
                config_path=CONFIG_YAML_PATH,
                params_path=PARAM_YAML_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig :
        ingestion_config = self.config.data_ingestion
        create_directories([ingestion_config.root_dir])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=ingestion_config.root_dir,
            source_url=ingestion_config.source_url,
            local_data_file= ingestion_config.local_data_file,
            unzip_dir= ingestion_config.unzip_dir
        )
        return data_ingestion_config
    
class ConfigurationManagerT:
    def __init__(self , configPath = CONFIG_YAML_PATH , paramsPath = PARAM_YAML_PATH):
        self.config = read_yaml(configPath)
        self.params = read_yaml(paramsPath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_transformationConfig(self) -> DataTransformationConfig:
            config=self.config.data_transformation

            create_directories([config.root_dir])

            data_transformation_config=DataTransformationConfig(
                root_dir=config.root_dir,
                data_path=config.data_path,
                tokenizer_name=config.tokenizer_name
            )

            return data_transformation_config
        
class ConfigurationManagerMT:
    def __init__(self , config= CONFIG_YAML_PATH , params = PARAM_YAML_PATH):
        self.config = read_yaml(config) 
        self.params = read_yaml(params)
        
        
        
        # create_directories([self.config.root_dir])
        
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        get_model_trainer = self.config.model_trainer
        create_directories([get_model_trainer.root_dir])
        get_model_trainer_config = ModelTrainerConfig(
            root_dir=get_model_trainer.root_dir,
            data_path=get_model_trainer.data_path,
            model_name=get_model_trainer.model_name
            
        )
        
        return get_model_trainer_config
    
    
    
class ConfigurationManagerME:
    def __init__(self , config = CONFIG_YAML_PATH , params = PARAM_YAML_PATH ):
        self.config = read_yaml(config)
        self.params = read_yaml(params)
        
        create_directories([self.config.artifacts_root])
        
    def get_model_eval_config(self) -> ModelEvaluationConfig:
            model_eval_conf = self.config.model_evaluation
            
            create_directories([model_eval_conf.root_dir])
            
            model_eval_config = ModelEvaluationConfig(
            root_dir=model_eval_conf.root_dir,
            data_path=model_eval_conf.data_path,
            model_path=model_eval_conf.model_path,
            tokenizer=model_eval_conf.tokenizer_name,
            metric_file_name=model_eval_conf.metric_file_name
            )
            
            return model_eval_config
            