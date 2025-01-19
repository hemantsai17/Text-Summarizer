from src.Text_Summarizer.entity import ModelEvaluationConfig
from src.Text_Summarizer.config.configuration import ConfigurationManagerME
from src.Text_Summarizer.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def evaluate_model():
        config = ConfigurationManagerME()
        modelEvalCOnfgi = config.get_model_eval_config()
        model_eval = ModelEvaluation(config=modelEvalCOnfgi)
        model_eval.evaluate()