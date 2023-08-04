# Hugging Face - Translation

This is a simple example of how to use the Hugging Face Hub for translating text.

## The basics

1. Must have Python3.
2. Get repository
```bash
git clone https://github.com/msuliot/huggingface_translation.git 
```
3. use pip3 to install any dependencies.
```bash
pip3 install -r requirements.txt
```

## Hugging Face Access Token

You'll need to sign up for an account on https://huggingface.co/ and get an access token.
Make sure to get an access token key from https://huggingface.co/settings/tokens

Create a ".env" file and put your access token in that file
```bash
HUGGINGFACEHUB_API_TOKEN = 'hf_XXXXXXXX'
```

# Instructions:

There are three different examples of how to use the Hugging Face Hub.

## 1. Run the API script
```bash
python3 api.py
```

## 2. Run the pipeline script
```bash
python3 pipeline.py
```

## 3. Run the local script
```bash
python3 local.py
```
This will download the model and tokenizer to your local machine and run on your local machine.
Supported tensors are 
- PyTorch 
- TensorFlow

## Hugging Face Hub API 
https://huggingface.co/t5-large
- modelId: t5-large
- pipeline_tag: translation
- library_name: transformers
- architectures: T5ForConditionalGeneration
- transformersInfo: auto_model: AutoModelForSeq2SeqLM
- transformersInfo: pipeline_tag: text2text-generation
- transformersInfo: processor: AutoTokenizer
- task_specific_params:
- - summarization - max_length: 200 - prefix: summarize: 
- - translation_en_to_de - max_length: 300 - prefix: translate English to German: 
- - translation_en_to_fr - max_length: 300 - prefix: translate English to French: 
- - translation_en_to_ro - max_length: 300 - prefix: translate English to Romanian: