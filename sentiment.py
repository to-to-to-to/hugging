from transformers import pipeline
import argparse as ap
import sys
import utils
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

SENT_MODEL = "distilbert-base-uncased-finetuned-sst-2-english"


def sentiment_pipeline(text, classifier):
    sentiments = classifier(text)
    return sentiments


def print_sents(text, sentiments):
    if(type(text) == str):
        list_text = []
        list_text.append(text)
        text = list_text.copy()
    for i, j in zip(text, sentiments):
        print(f"{i} , {j['label']}, {j['score']}")


def build_sent(text):
    sent_classifier = pipeline("sentiment-analysis", model=SENT_MODEL)
    sentiments = sentiment_pipeline(text, sent_classifier)
    print_sents(text, sentiments)


def main():
    parser = ap.ArgumentParser(description=utils.descriptions["sentiment"])
    parser.add_argument('text', type=str, default=sys.stdin)
    args = parser.parse_args()
    # print(args.text)

    try:
        text = utils.read_file_lines(args.text)
        # print(text)
    except FileNotFoundError:
        print("No file found treating input as plain text")
        text = args.text
        # print(text)
    build_sent(text)


if __name__ == "__main__":
    main()
