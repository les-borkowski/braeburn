import requests
import re
from bs4 import BeautifulSoup
from typing import Counter
import string


def get_words(url_address):
    # parse the data from url and return sorted dictionary
    web_page_data = get_data_from_url(url_address)
    text_string = get_text_from_html(web_page_data)
    text_clean = split_string(text_string)
    counted_dict = count_list_and_sort(text_clean)
    return counted_dict


def get_data_from_url(url_address):
    # retrieve data from given url
    web_page_data = requests.get(url_address)
    return web_page_data.content


def get_text_from_html(web_page_data):
    # remove html tags, return string of words from the <body> using lxml parser
    soup = BeautifulSoup(web_page_data, 'lxml')
    words_string = soup.body.get_text(" ", strip=True)
    return words_string


def split_string(data):
    # split string into words, words to lowercase
    lcase_string = data.lower()
    list_words = re.sub(r'['+string.punctuation+']', '', lcase_string).split()
    return list_words


def count_list_and_sort(string):
    # split and count words, then return a dict sorted by frequency (desc)
    # words = string.split()
    words_counter = Counter(string)
    words_sorted_dict = dict(words_counter.most_common(100))
    return words_sorted_dict
