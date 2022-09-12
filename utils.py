from mlhub.pkg import get_cmd_cwd
import trafilatura
import re


def check_url(url):
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$" # noqa : E501
    return re.match(url_pattern, url)


def read_file(file_name, demo):
    if demo:
        path = file_name
    else:
        path = f"{get_cmd_cwd()+'/'+file_name}"
    file = open(path)
    text = file.read()
    return text


def read_url(url):
    downloaded = trafilatura.fetch_url(url)
    pretty_str = trafilatura.extract(downloaded)
    return pretty_str


def read_file_lines(file_name):
    path = f"{file_name}"
    with open(path) as f:
        lines = [line.rstrip() for line in f]  # ignore \n
    return lines


descriptions = {"summarize": 'summarize a given piece of text',
                "sentiment": 'provide the sentiment ((pos | neg), score) \
                              of a given piece of text',
                "demo":      'provide a demo of the commands implemented so far' # noqa : E501
                }

commands = ["sentiment", "summarize"]
