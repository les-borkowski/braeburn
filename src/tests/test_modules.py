import requests
from src.url_validator import UrlValidator
from src.get_and_count_words import get_data_from_url, split_string, count_list_and_sort, get_text_from_html


def test_url_validator():
    invalid_url_1 = "www.bbc.co.uk"
    invalid_url_2 = "random string"
    valid_url = "https://bbc.co.uk"

    assert UrlValidator(invalid_url_1) is False
    assert UrlValidator(invalid_url_2) is False
    assert UrlValidator(valid_url) is True


def test_get_data_from_url(monkeypatch):
    my_url = "www.example.com"

    class MockResponse:

        def __init__(self, content):
            self.status_code = 200
            self.url = 'http://httpbin.org/get'
            self.headers = {'blaa': '1234'}
            self.content = content

        def json(self):
            return self.content

    monkeypatch.setattr(
        requests,
        'get',
        lambda *args, **kwargs: MockResponse({'content': my_url})
    )

    assert get_data_from_url(my_url) == {'content': my_url}


def test_get_text_from_html():
    mock_data = """<!DOCTYPE html> <html> <head> <title>Sample page</title> </head> <body> <h1>Kitten</h1> <p>Fluffy fluffy mittens</p> </body> </html>"""
    desired_output = "Kitten Fluffy fluffy mittens"
    data = get_text_from_html(mock_data)
    assert data == desired_output


def test_split_string():
    string_quotes = "'Hello World' - said Snake"
    string_noquotes = ["hello", "world", "said", "snake"]

    string_clean = split_string(string_quotes)
    assert string_clean == string_noquotes


def test_count_list_and_sort():
    test_string_2 = ["hello", "hello", "said", "snake"]
    desired_result_2 = {'hello': 2, 'said': 1, 'snake': 1}

    string_sorted = count_list_and_sort(test_string_2)
    assert string_sorted == desired_result_2
