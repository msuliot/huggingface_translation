import os
from transformers import pipeline, AutoTokenizer
from transformers import T5ForConditionalGeneration, TFT5ForConditionalGeneration

from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN')
os.environ['TOKENIZERS_PARALLELISM'] = 'true'


def set_local_vars():
    model_name = "t5-large" 
    pipeline_task = "translation_en_to_fr"
    return model_name, pipeline_task


def hf_local(model_name, pipeline_task, text):
    # This will download the model and tokenizer to your local machine and run on your local machine. 
    # saved and cached ~/.cache/huggingface
    tokenizer = AutoTokenizer.from_pretrained(model_name, return_tensors="pt") # return_tensors="pt" or "tf"
    model = T5ForConditionalGeneration.from_pretrained(model_name) # T5ForConditionalGeneration or TFT5ForConditionalGeneration
    pipe = pipeline(pipeline_task, model=model, tokenizer=tokenizer, max_length=300)
    output = pipe(text)
    return output


def main():
    model_name, pipeline_task = set_local_vars()

    text = """translate English to French: I love watching Michael's videos. Subscribe!"""
    
    return_value = hf_local(model_name, pipeline_task, text)
    print(return_value)

if __name__ == "__main__":
    main() 