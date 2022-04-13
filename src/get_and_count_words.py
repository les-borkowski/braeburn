import requests
import re
from bs4 import BeautifulSoup
from typing import Counter


def get_words(url_address):
    # parse the data from url and return sorted dictionary
    web_page_data = get_data_from_url(url_address)
    text_string = get_text_from_html(web_page_data)
    text_clean = remove_quotes(text_string)
    counted_dict = count_list_and_sort(text_clean)
    return counted_dict


def get_data_from_url(url_address):
    # retrieve data from given url
    web_page_data = requests.get(url_address)
    return web_page_data.content


def get_text_from_html(web_page_data):
    # remove html tags and return string of words from the <body> of the html using lxml parser
    # page_data = web_page_data.text
    soup = BeautifulSoup(web_page_data, 'lxml')
    words_string = soup.body.get_text(" ", strip=True)
    return words_string


def remove_quotes(string):
    # remove quotes and special characters, words to lowercase
    list_words = re.sub('[\'.:?\-\']', '', string).lower()
    return list_words


def count_list_and_sort(string):
    # split and count words, then return a dict sorted by frequency (desc)
    words = string.split()
    words_counter = Counter(words)
    words_sorted_dict = dict(words_counter.most_common())
    return words_sorted_dict

