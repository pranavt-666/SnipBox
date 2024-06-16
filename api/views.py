from django.shortcuts import render
from api import models
from api import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet,mixins


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



class SnippetModelView(ViewSet):

    # serializer_class = serializers.SnippetSerializer
    # queryset = models.Snippet.objects.all()
    # # http_method_names = ['get', 'post',]
    def create(self, request, *args, **kwargs):
        user = request.user
        tag = request.data.get('tag')
        serializer = serializers.SnippetSerializer(data=request.data,
        context={'user':user, 'tag':tag})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors) 

    def retrieve(self, request, *args, **kwargs):
        snippet_id = kwargs.get('pk')
        snippet = models.Snippet.objects.get(id=snippet_id)
        serialzi
        return Response(data)

        
    
