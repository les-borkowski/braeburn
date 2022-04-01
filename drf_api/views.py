from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def health(request):
    data = {"health": "OK"}
    return JsonResponse(data)

@api_view(['GET'])
def api(request):
    
    url = request.query_params.get('url', None)
    data = {"url": url}
    return JsonResponse(data)