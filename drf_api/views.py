from django.http import JsonResponse
from rest_framework.decorators import api_view
from src.url_validator import UrlValidator
from src.get_and_count_words import get_words
import logging
from datetime import datetime

# logging setup
logging.basicConfig(filename='api.log', level=logging.INFO)


@api_view(['GET'])
def health(request):
    # health endpoint
    data = {"health": "OK"}
    return JsonResponse(data)


@api_view(['GET'])
def api(request):
    # get url address and return words between html tags, log the result
    url = request.query_params.get('url', None)
    if UrlValidator(url):
        processed_words = get_words(url)
        data = {"data": processed_words}
        logging.info(f"{datetime.now()} | {url} | {data}")
        return JsonResponse(data)
    else:
        data = {"message": "Url Invalid"}
        logging.error(f"{datetime.now()} | {url} | {data}")
        return JsonResponse(data)
