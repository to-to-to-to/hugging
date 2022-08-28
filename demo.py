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
    os.system("python3 sentiment.py sent_text.txt")

if(args.command == "summarize"):
    os.system("python3 summarize.py microsoft_text.txt --min_len 50 --max_len 100") # noqa : E501