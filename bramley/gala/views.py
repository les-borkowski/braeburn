from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import status, generics, permissions
from gala.models import Query
from gala.serializers import QuerySerializer, UserSerializer
from django.contrib.auth.models import User
import json
import subprocess


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-list', request=request, format=format),
        'queries': reverse('query-list', request=request, format=format)
    })

class QueryList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    
    def get(self, request, format=None):
        user = self.request.user
        if user.is_superuser:
            queries = Query.objects.all()
        else:
            queries = Query.objects.filter(owner=user)
            
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        url = self.request.POST.get('url')
        words = self.get_words(url)
        
        serializer = QuerySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(data=words, owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # fetch words based on url in the post request
    def get_words(self, url):
        r = subprocess.check_output(['python', 'braeburn.py', f'{url}'], universal_newlines=True)
        json_data = json.loads(r)
        # if response from braeburn.py is valid, add data to the db
        if json_data['status'] == '10':
            result = json_data['data']
            return result
        
    

class QueryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        
        user = self.request.user
        if user.is_superuser:
            return Query.objects.all()
        else:
            return Query.objects.filter(owner=user)
    
    serializer_class = QuerySerializer

    
class UserList(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer
     