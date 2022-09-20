import utils
import argparse as ap
import os

parser = ap.ArgumentParser(description=utils.descriptions["demo"])
parser.add_argument("command", type=str)
args = parser.parse_args()

if(args.command not in utils.commands):
    print(f"invalid command entered valid commands are {utils.commands}")
    exit(1)

if(args.command == "sentiment"):
    import sentiment
    introduction = """Sentiment analysis is the process of determining whether a piece of text is positive, negative, or neutral. This can be done using a variety of methods, but one popular approach is to use a transformer model. We use the HuggingFace library to help us build our models. This demo function will show you the input/output of a simple transformer model that predicts the sentiment of a statement. """
    print(introduction)
    print("Enter a statement to be analyzed:", end=' ')
    statement = input()
    print("Analyzing...")
    sentiment.build_sent(statement)

if(args.command == "summarize"):
    import summarize
    os.system("python3 summarize.py microsoft_text.txt --min_len 50 --max_len 100 --demo True") # noqa : E501
