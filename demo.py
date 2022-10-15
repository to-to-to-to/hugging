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
    sentiments = []
    for i in text:
        sentiments.append((sentiment.build_sent(i)))
    mlcat(title="Corresponding Sentiments", text="", end="")
    for i in sentiments:
        print("{:.2f}".format(sentiment.output_sent(i)))


if(args.command == "summarize"):
    introduction = """Machine learning text summarization works by taking a \
        large amount of text and reducing it to its most important points. \
        This is done by using algorithms that identify the main ideas in the \
        text and then create a summary based on those ideas. \
        This is achieved by transformers by training a model on a large\
        amount of data and then fine-tuning it to be able to summarise text. \
        We use the hugging face repository to leverage these transfomers. \
        This demo function will walk you through a simple example and \
        translate microsoft_text.txt which is present in the /.mluhub \
        directory for reference. """
    mlcat(title="Summarization pipeline showcase", text=introduction) # noqa : E501
    mlask(begin="", end="\n",
          prompt="Press Enter to display the summary of microsoft_text.txt")
    print("Analysing...")
    mlcat(title="Summary of microsoft_text.txt", text="", end="")
    os.system("python3 summarize.py microsoft_text.txt --min_len 50 --max_len 100 --demo True") # noqa : E501
