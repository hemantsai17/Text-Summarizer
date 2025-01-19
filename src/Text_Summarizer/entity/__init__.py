from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir : Path 
    source_url : Path
    local_data_file : Path
    unzip_dir : Path
    
@dataclass
class DataTransformationConfig:
    root_dir: Path 
    data_path : Path
    tokenizer_name: Path
    
@dataclass
class ModelTrainerConfig:
    root_dir: Path
    data_path : Path
    model_name : Path
    
from pathlib import Path
from dataclasses import dataclass

@dataclass
class ModelEvaluationConfig:
    root_dir : Path 
    data_path : Path
    model_path : Path
    tokenizer : Path
    metric_file_name : Path