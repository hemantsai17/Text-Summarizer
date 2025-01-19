import os
from src.Text_Summarizer.config.configuration import ConfigurationManagerME
from transformers import AutoModelForSeq2SeqLM , AutoTokenizer , pipeline


class PredictionPipeline:
    def __init__(self):
        config_manager = ConfigurationManagerME()  # Create an instance
        self.config = config_manager.get_model_eval_config()
    
    def predict(self,text):
        
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer)
        model_name = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)
        
        
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}



        # sample_text = dataset_samsum["test"][0]["dialogue"]

        # reference = dataset_samsum["test"][0]["summary"]

        pipe = pipeline("summarization", model=model_name,tokenizer=tokenizer)

        ##
        print("Dialogue:")
        print(text)


        # print("\nReference Summary:")
        # print(reference)


        print("\nModel Summary:")
        print(pipe(text, **gen_kwargs)[0]["summary_text"])
        return pipe(text, **gen_kwargs)[0]["summary_text"]