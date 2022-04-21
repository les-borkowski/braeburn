from rest_framework import serializers
from gala.models import Query
from django.contrib.auth.models import User

class QuerySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Query
        fields = ['id', 'url', 'data', 'owner', 'created']
        
class UserSerializer(serializers.ModelSerializer):
    queries = serializers.PrimaryKeyRelatedField(many=True, queryset=Query.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'username', 'queries']