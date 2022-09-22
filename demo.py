import utils
import argparse as ap
import os
from mlhub.pkg import mlask, mlcat

parser = ap.ArgumentParser(description=utils.descriptions["demo"])
parser.add_argument("command", type=str)
args = parser.parse_args()

if(args.command not in utils.commands):
    print(f"invalid command entered valid commands are {utils.commands}")
    exit(1)

if(args.command == "sentiment"):
    import sentiment
    text = utils.read_file_lines("sent_text.txt")
    introduction = """Sentiment analysis is the process of determining whether
    a piece of text is positive, negative, or neutral.
    This can be done using a variety of methods, but one popular approach
    is to use a transformer model. We use the HuggingFace library to help us
    build our models. This demo function will show you the input/output of a
    simple transformer model that predicts the sentiment of a statement. """

    mlcat(title="Sentiment pipeline showcase", text=introduction)
    mlask(begin="\n", end="\n",
          prompt="Press Enter to display the sentences")
    sents = utils.print_file_lines("sent_text.txt")
    mlcat(title="Sentences", text="", end="")
    print(sents)
    mlask(begin="", end="\n",
          prompt="Press Enter to display the sentiments")
    print("Analysing...")
    sentiments = sentiment.build_sent(text)
    formatted_sents = sentiment.print_sents(text, sentiments)
    mlcat(title="Sentiments", text="", end="")
    for i in formatted_sents:
        print(i)

if(args.command == "summarize"):
    os.system("python3 summarize.py microsoft_text.txt --min_len 50 --max_len 100 --demo True") # noqa : E501
