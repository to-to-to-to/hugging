from mlhub.pkg import get_cmd_cwd
import trafilatura
import re


def check_url(url):
    """check if the url is valid

    Args:
        url (str): url to be checked

    Returns:
        bool: True if url is valid else False
    """
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$" # noqa : E501
    return re.match(url_pattern, url)


def read_file(file_name, demo=False):
    """read file and return the text

    Args:
        file_name (str): file name to be read
        demo (bool): if demo is true then read the file from the demo folder

    Returns:
        str: text from the file
    """
    if demo:
        path = file_name
    else:
        path = f"{get_cmd_cwd()+'/'+file_name}"
    file = open(path)
    text = file.read()
    return text


def read_url(url):
    """read url and return the text"""
    downloaded = trafilatura.fetch_url(url)
    pretty_str = trafilatura.extract(downloaded)
    return pretty_str


def read_file_lines(file_name):
    """read file and return the text as list of lines """
    path = f"{file_name}"
    with open(path) as f:
        lines = [line.rstrip() for line in f]  # ignore \n
    return lines


def print_file_lines(path):
    """ prints the lines of a file

    Args:
        path (str): path of the file

    Returns:
        str: text from the file on each line
    """
    sents = ""
    with open(path) as f:
        sents += (f.read())
        sents += ("\n")
    return sents


def format_text(text):
    """format the text to be printed

    Args:
        text (str): text to be formatted

    Returns:
        list: list of formatted sentences
    """
    text = text.replace(" .", ". ")
    text = text.replace(". ", ".")
    # split text into sentences
    sentences = text.split(".")
    # remove empty sentences
    sentences = [s.strip() for s in sentences if s]
    # capitalise only first letter of each sentence
    formatted_sents = [(sentence[0].upper() + sentence[1:] + '.') for sentence in sentences] # noqa : E501
    return formatted_sents


descriptions = {"summarize": 'summarize a given piece of text',
                "sentiment": 'provide the sentiment ((pos | neg), score) \
                              of a given piece of text',
                "demo":      'provide a demo of the commands implemented so far' # noqa : E501
                }

commands = ["sentiment", "summarize"]
