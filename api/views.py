from django.shortcuts import render
from api import models
from api import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet


# Create your views here.


class TagView(ViewSet):
    
    def list(self, request, *args, **kwargs):
        queryset = models.Tag.objects.all()
        serializer = serializers.TagSerializer(queryset, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        tag_id = kwargs.get('pk')
        tag = models.Tag.objects.get(id=tag_id)
        snippet = models.Snippet.objects.filter(tag=tag)
        serializer = serializers.SnippetSerializer(snippet, many=True)
        return Response(data=serializer.data)


class SnippetModelView(ModelViewSet):

    serializer_class = serializers.SnippetSerializer
    queryset = models.Snippet.objects.all() 

    # def create(self, )
        
    
