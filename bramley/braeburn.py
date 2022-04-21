from collections import Counter
import unittest
import requests
import sys
import re
from datetime import datetime
import json
import logging
import argparse

from bs4 import BeautifulSoup

# logging setup
logging.basicConfig(filename='braeburn_info.log',level=logging.INFO)

# argparse setup
parser = argparse.ArgumentParser()
parser.add_argument('url', help='Enter full url: https://example.com')
parser.add_argument( '-u', '--unittest', help='Show unit tests', action="store_true")

args = parser.parse_args()
if args.unittest:
    print('Unit tests on:')
# values for testing 
TEST_URL = 'http://bbc.co.uk'

# URL validation
# from https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not Django url validation regex
REGEX = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

# output data
class OutputData:
    def __init__(self, status, message, url, data):
        self.status = status
        self.message = message
        self.url = url
        self.data = data
            
    def return_json(self):
        json_string = json.dumps(self.__dict__, indent=4, ensure_ascii=False)
        
        logging.info(f'{self.status} | {self.message} | {self.url} | {datetime.now()}')
        
        return json_string        
             
    def error_message(self):
        logging.error(f'Error {self.status}: {self.message} | {datetime.now()}')
        print(f'Error {self.status}: {self.message}')
    
    def __str__(self):
        return f'{self.status} | {self.message} | {self.url}'

# this function is redundant when api is being used
def is_valid(address):
        
        if(re.match(REGEX, address) is not None):
            return True
              
        
def get_request(address):
    
    # headers info here
    headers ={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8'
    }
   
    # send http request and return response
    r = requests.get(address, headers=headers)
    try: 
        r.raise_for_status()
        
    except requests.exceptions.HTTPError as e:
        error_code = '02'
        error = OutputData(error_code, e, address, None).return_json()
        sys.exit(error)
    
    return r
    
# web data parser
class WebPageData:
        
        def __init__(self, httpresponse):
            self.response = httpresponse
        
        def get_text_from_html(self, response):
            data = self.response
            soup = BeautifulSoup(data.text, 'lxml')
            words_string = soup.get_text(" ", strip=True)

            return words_string
      
        def parse_string_to_dict_and_count(self, string):
            
            words = re.sub('[\'0-9.:?\-\']', '', string).split()
            
            words_counter = Counter(words)
            words_sorted_dict = dict(words_counter.most_common())
            return words_sorted_dict
            
     
        def parse_data_to_dict(self):
            
            words_string = self.get_text_from_html(self.response)
            counted_words_dict = self.parse_string_to_dict_and_count(words_string)
            # self.filter_words(counted_words_dict)
            
            return counted_words_dict 
            

def main():
    
    # add small script to measure performance - time to get response   
    url = args.url
    
    if is_valid(url):
        response = get_request(url)
        
        #  add small script to measure performance - time to process data
        list_of_words = WebPageData(response)
        counted_words = list_of_words.parse_data_to_dict()
        
        output = OutputData('10', 'Success', url, counted_words)
        result = output.return_json()
        
        # for testing: save data to file
        # with open('data.json', 'w', encoding='utf-8') as f:
        #     f.write(result)
        
        return result
    
    else:
        error_code = '02'
        error_text = f"URL is not valid -- example: http://example.co.uk"
        error = OutputData(error_code, error_text, None, None).return_json()
        return error
        # return url
   
class TestInputData(unittest.TestCase):
    
    # test if input exists (argv[1])
    def test_input(self):
        url = args.url
        self.assertIsNotNone(url)
    
    # check if response is received
    def test_http_response(self):
        url = TEST_URL
        response = get_request(url)
        self.assertIsNotNone(response)
    
class TestDataParsing(unittest.TestCase):
            
    # check if string is parsed to a dict
    def test_response_to_string(self):
        
        test_url = TEST_URL
        r = get_request(test_url)
        
        test = WebPageData(r).get_text_from_html(r)
        self.assertTrue(type(test) == str)
        
    # test if response is parsed and filtered correctly 
    def test_string_to_dict(self):
        test_url = TEST_URL
        r = get_request(test_url)
        test_instance = WebPageData(r).parse_data_to_dict()
        self.assertTrue(type(test_instance) == dict and 's' not in test_instance)
        
    
if __name__ == '__main__':
    if args.unittest:
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    sys.stdout.write(main())
    sys.stdout.flush()
    sys.exit()
    