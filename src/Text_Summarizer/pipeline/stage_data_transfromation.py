from src.Text_Summarizer.config.configuration import ConfigurationManagerT
from src.Text_Summarizer.components.data_transformation1 import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation():
        config_manager = ConfigurationManagerT()
        data_transformation_config1 = config_manager.get_data_transformationConfig()

        data_transformation = DataTransformation(config=data_transformation_config1)

        data_transformation.convert()