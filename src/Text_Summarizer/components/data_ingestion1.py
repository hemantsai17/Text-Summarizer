import os 
import urllib.request as request
import zipfile
from src.Text_Summarizer.logging import logger
from src.Text_Summarizer.entity import DataIngestionConfig

class DataIngestion:
    def __init__(self , config : DataIngestionConfig):
        self.config = config
        
    def download_file(self):
       if not os.path.exists(self.config.local_data_file):
           filename , headers = request.urlretrieve(url=self.config.source_url, filename=self.config.local_data_file)
           
           logger.info(f"File:{filename} Downnloaded")
       else:
           logger.info(f'file already exists')
           
    def extract_zip_file(self):
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir , exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file , 'r') as zip_ref:
            zip_ref.extractall(unzip_dir)
            
            

           