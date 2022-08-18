from mlhub.pkg import get_cmd_cwd
import trafilatura
import re


def check_url(url):
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    return re.match(url_pattern, url) 

def read_file(file_name):
    path = f"{get_cmd_cwd()+'/'+file_name}"
    file = open(path)
    text = file.read()
    return text

def read_url(url):
    downloaded = trafilatura.fetch_url(url)
    pretty_str = trafilatura.extract(downloaded)
    return pretty_str

