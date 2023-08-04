import os
from transformers import pipeline
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN')
os.environ['TOKENIZERS_PARALLELISM'] = 'true'


def set_local_vars():
    model_name = "t5-large"
    pipeline_task = "translation_en_to_fr"  # translation_XX_to_YY, summarization 
    return model_name, pipeline_task


def hf_pipeline(model_name, pipeline_task, text):
    pipe = pipeline(task=pipeline_task, model=model_name, max_length=300)
    output = pipe(text)
    return output


def main():
    model_name, pipeline_task = set_local_vars()
    
    text = """translate English to French: I love watching Michael's videos. Subscribe!"""
    
    return_value = hf_pipeline(model_name, pipeline_task, text)
    print(return_value) 


if __name__ == "__main__":
    main() 