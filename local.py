import os
from transformers import pipeline, AutoTokenizer
from transformers import T5ForConditionalGeneration, TFT5ForConditionalGeneration

from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN')
os.environ['TOKENIZERS_PARALLELISM'] = 'true'


def set_local_vars():
    model_name = "t5-large" 
    pipeline_task = "translation_XX_to_YY"
    return model_name, pipeline_task


def hf_local(model_name, pipeline_task, text):
    # This will download the model and tokenizer to your local machine and run on your local machine. 
    # saved and cached ~/.cache/huggingface
    tokenizer = AutoTokenizer.from_pretrained(model_name, return_tensors="pt",model_max_length=300) # return_tensors="pt" or "tf"
    model = T5ForConditionalGeneration.from_pretrained(model_name,) # T5ForConditionalGeneration or TFT5ForConditionalGeneration
    pipe = pipeline(pipeline_task, model=model, tokenizer=tokenizer)
    output = pipe(text)
    return output


def main():
    model_name, pipeline_task = set_local_vars()

    text = "English to French: Subscribe to Michael's videos. They are great."
    
    return_value = hf_local(model_name, pipeline_task, text)
    print(return_value)

if __name__ == "__main__":
    main() 