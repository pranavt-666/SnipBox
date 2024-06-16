from django.shortcuts import render
from api import models
from api import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet,mixins
from rest_framework.decorators import action
from rest_framework.reverse import reverse


class TagView(ViewSet):
    """
    ViewSet for managing Tag objects.
    
    list:
    Retrieves a list of all tags.

    retrieve:
    Retrieves a specific tag and all associated snippets.
    """
    def list(self, request, *args, **kwargs):
        try:
            queryset = models.Tag.objects.all()
            serializer = serializers.TagSerializer(queryset, many=True)
            return Response(data=serializer.data)
        except Exception as msg:
            msg = str(msg)
            return Response({'res':msg})

    def retrieve(self, request, *args, **kwargs):
        try:
            tag_id = kwargs.get('pk')
            tag = models.Tag.objects.get(id=tag_id)
            snippet = models.Snippet.objects.filter(tag=tag)
            serializer = serializers.SnippetSerializer(snippet, many=True)
            return Response(data=serializer.data)
        except Exception as msg:
            msg = str(msg)
            return Response({'res':msg})


class SnippetModelView(ViewSet):
    """
    ViewSet for managing Snippet objects.
    
    create:
    Create a new snippet.

    retrieve:
    Retrieve a specific snippet.

    update:
    Update a specific snippet.

    destroy:
    Delete a specific snippet.

    overview:
    Retrieve the total count and list of all snippets.
    """

    def create(self, request, *args, **kwargs):
        try:
            user = request.user
            tag = request.data.get('tag')
            serializer = serializers.SnippetSerializer(data=request.data,
            context={'user':user, 'tag':tag})
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors) 
        except Exception as msg:
            msg = str(msg)
            return Response({'res':msg})

    def retrieve(self, request, *args, **kwargs):
        try:
            snippet_id = kwargs.get('pk')
            snippet = models.Snippet.objects.get(id=snippet_id)
            if snippet.created_user == request.user:
                serializer = serializers.SnippetSerializer(snippet)
                return Response(data=serializer.data)
            else:
                return Response({'res':'you are not the user to retrieve'})
        except Exception as msg:
            msg = str(msg)
            return Response({'res':msg})   

    def update(self, request, *args, **kwargs):
        try:
            snippet_id = kwargs.get('pk')
            snippet = models.Snippet.objects.get(id=snippet_id)
            # if snippet:
            serializer = serializers.SnippetSerializer(data=request.data, instance=snippet)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)
        except Exception as msg:
            msg = str(msg)
            return Response({'res':msg})

    def destroy(self, request, *args, **kwargs):
        try:
            snippet_id = kwargs.get('pk')
            snippet = models.Snippet.objects.get(id=snippet_id)
            snippet.delete()
            queryset = models.Snippet.objects.all()
            serializer = serializers.SnippetSerializer(queryset, many=True)
            return Response(data=serializer.data)
        except Exception as msg:
            msg = str(msg)
            return Response({'res':msg})

    @action(detail=False, methods=['get'])
    def overview(self, request):
        try:
            snippets = models.Snippet.objects.all()
            total_count = snippets.count()
            snippet_list = [{
                'id': snippet.id,
                'note': snippet.note,
                'url': reverse('snippets-detail', args=[snippet.id], request=request)
            } for snippet in snippets]
            return Response({
                'total_count': total_count,
                'snippets': snippet_list
            })
        except Exception as msg:
            msg = str(msg)
            return Response({'res':msg})
        
    
