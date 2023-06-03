import spacy
print(4)
# from summarizer import Summarizer,TransformerSummarizer
# bert_model = Summarizer()
# bert_summary = ''.join(bert_model(body, min_length=6))
# print(bert_summary)
# GPT2_model =
TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
# full = ''.join(GPT2_model(body, min_length=6))
# print(full)
from transformers import pipeline
# use bart in pytorch
# summarizer = pipeline("summarization")
# ptorch = summarizer("An apple a day, keeps the doctor away",min_length=5, max_length=20)
# use t5 in tf
def sumari(body):
 summarizer = pipeline("summarization", model="t5-base",
tokenizer="t5-base", framework="tf")
 tflow = summarizer(body, min_length=100, max_length=200)
 print(tflow)
 return tflow