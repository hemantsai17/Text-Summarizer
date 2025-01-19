from src.Text_Summarizer.config.configuration import ConfigurationManager
from src.Text_Summarizer.components.data_ingestion1 import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def initiate_data_ingestion():
        config_manager = ConfigurationManager()
        data_ingestion_config1 = config_manager.get_data_ingestion_config()

        data_ingestion = DataIngestion(config=data_ingestion_config1)

        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
        

