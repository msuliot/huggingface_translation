import requests
import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file


def set_local_vars():
    model_name = "t5-large"
    api_url = f"https://api-inference.huggingface.co/models/{model_name}"
    return api_url


def hf_api(api_url, text):
    headers = {"Authorization": f"Bearer {hf_api_key}"}

    def query(payload):
        response = requests.post(api_url, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": text,
    })
    return output


def main():
    api_url = set_local_vars()

    text = "English to French: Subscribe to Michael's videos. They are great."
    
    return_value = hf_api(api_url, text)
    print(return_value)


if __name__ == "__main__":
    main() 