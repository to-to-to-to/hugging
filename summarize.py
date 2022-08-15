from transformers import pipeline
import argparse

def read_file(file_name):
    file = open(file_name)
    text = file.readlines()
    return text


def summarize_pipeline(text, summarizer, min_length, max_length):
    summarized_text = summarizer(text, min_length=min_length, max_length=max_length)
    return summarized_text


parser = argparse.ArgumentParser(description ='summarize a given piece of text')
  
parser.add_argument('text', metavar ='input_text', 
                    type = str,
                    help ='input text to be summarized')
  
parser.add_argument('--min_len',
                    type = int,
                    help ='minimum length of summarized text')

parser.add_argument('--max_len', 
                    type = int,
                    help ='maximum length of summarized text')
  
args = parser.parse_args()
min_length = 20
max_length = 50

if(args.min_len):
    min_length = args.min_len
if(args.max_len):
    max_length = args.max_len

# Calling it globally so we only have to call it once
# summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
summarizer = pipeline("summarization", model="t5-small", framework="pt")
text = read_file(args.text)

summarized_text = summarize_pipeline(text, summarizer=summarizer, min_length=min_length, max_length=max_length)
print(f"Summary of {args.text} between {min_length} and {max_length} words below:\n")
print(summarized_text[0]['summary_text'])
