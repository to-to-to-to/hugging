from transformers import pipeline
import argparse as ap
import sys
import utils
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

SENT_MODEL = "cardiffnlp/twitter-roberta-base-sentiment"


def sentiment_pipeline(text, classifier):
    sentiments = classifier(text)
    return sentiments


def output_sent(sentiments):
    first_sent = sentiments[0][0]
    second_sent = sentiments[0][1]
    if(first_sent['label'] == "LABEL_1"):  # neutral sent
        sent_val = first_sent['score'] - 1 + second_sent['score']
    else:
        sent_val = first_sent['score']
    return sent_val if first_sent['label'] == 'LABEL_2' else -1 * sent_val


def build_sent(text):
    sent_classifier = pipeline("sentiment-analysis", model=SENT_MODEL, top_k=None)  # noqa
    sentiments = sentiment_pipeline(text, sent_classifier)
    return sentiments


def parse_text():
    parser = ap.ArgumentParser(description=utils.descriptions["sentiment"])
    if(not sys.stdin.isatty()):
        text = sys.stdin.read()
        return text
    else:
        parser.add_argument('text', nargs="*", type=str)
        args = parser.parse_args()
        text = " ".join(args.text)
        if(len(text) == 0):  # no input given
            try:
                print("Enter text to be analysed or ctrl-d to quit\n")
                text = input("> ")
                return text
            except EOFError:
                sys.exit(0)
        if(text.endswith(("txt", "text", "TXT", "TEXT"))):
            try:
                text = utils.read_file(text)
                return text
            except FileNotFoundError:
                print(f"No file {text} found")
                sys.exit(0)
        else:
            return text


def main():
    text = parse_text()
    sentiments = build_sent(text)
    print("{:.2f}".format(output_sent(sentiments)))


if __name__ == "__main__":
    main()
