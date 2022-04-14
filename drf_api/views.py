from django.http import JsonResponse
from rest_framework.decorators import api_view
from src.url_validator import UrlValidator
from src.get_and_count_words import get_words


@api_view(['GET'])
def health(request):
    data = {"health": "OK"}
    return JsonResponse(data)


@api_view(['GET'])
def api(request):
    url = request.query_params.get('url', None)
    if UrlValidator(url):
        processed_words = get_words(url)
        data = {"data": processed_words}
        return JsonResponse(data)
    else:
        data = {"message": "Url Invalid"}
        return JsonResponse(data)
