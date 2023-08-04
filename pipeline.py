from transformers import pipeline

import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file
model_name = os.getenv('MODEL_NAME') # model name for huggingface.co in .env file
pipeline_task = os.getenv('PIPELINE_TASK') # pipeline task for huggingface.co in .env file
os.environ['TOKENIZERS_PARALLELISM'] = 'true'


def hf_pipeline(text):
    pipe = pipeline(task=pipeline_task, model=model_name, max_length=300)
    output = pipe(text)
    return output


def main():
    text = "English to French: Subscribe to Michael's videos. They are great."
    return_value = hf_pipeline(text)
    print(return_value) 


if __name__ == "__main__":
    main() 