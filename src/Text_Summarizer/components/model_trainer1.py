from transformers import TrainingArguments, Trainer , AutoModelForSeq2SeqLM , AutoTokenizer,DataCollatorForSeq2Seq
from src.Text_Summarizer.logging import logger
from datasets import load_from_disk
import torch
import os
from src.Text_Summarizer.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self , config : ModelTrainerConfig):
        self.config = config
    
    def train1(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_name)  #load a tokenizer

        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_name)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        dataset_samsum_pt = load_from_disk(self.config.data_path)
        
        trainer_args = TrainingArguments(
        output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
        per_device_train_batch_size=1, per_device_eval_batch_size=1,
        weight_decay=0.01, logging_steps=10,
        evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
        gradient_accumulation_steps=16
        )
        
        trainer = Trainer(model=model_pegasus, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["train"],
                  eval_dataset=dataset_samsum_pt["validation"])
        
        
        trainer.train()
        
        ## Save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"Trained_pegasus-samsum-model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"trained_tokenizer"))