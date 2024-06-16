from django.shortcuts import render
from api import models
from api import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet,mixins
from rest_framework.decorators import action
from rest_framework.reverse import reverse


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
        if snippet.created_user == request.user:
            serializer = serializers.SnippetSerializer(snippet)
            return Response(data=serializer.data)
        else:
            return Response({'res':''})
        
    def update(self, request, *args, **kwargs):
        snippet_id = kwargs.get('pk')
        snippet = models.Snippet.objects.get(id=snippet_id)
        serializer = serializers.SnippetSerializer(data=request.data, instance=snippet)
        return Response(data=serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        snippet_id = kwargs.get('pk')
        snippet = models.Snippet.objects.get(id=snippet_id)
        snippet.delete()
        queryset = models.Snippet.objects.all()
        serializer = serializers.SnippetSerializer(data=queryset, many=True)
        return Response(data=serializer.data)

    @action(detail=False, methods=['get'])
    def overview(self, request):
        snippets = self.get_queryset()
        total_count = snippets.count()
        snippet_list = [{
            'id': snippet.id,
            'note': snippet.note,
            'url': reverse('todo-detail', args=[snippet.id], request=request)
        } for snippet in snippets]
        
        return Response({
            'total_count': total_count,
            'snippets': snippet_list
        })
        
    
