from rest_framework import serializers
from api import models


class TagSerializer(serializers.Serializer):
    title = serializers.CharField()


class SnippetSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(read_only=True)
    updated_time = serializers.DateTimeField(read_only=True)
    # created_user = serializers.CharField(read_only=True)
    # tag = serializers.CharField(read_only=True)

    class Meta:
        model = models.Snippet
        fields = ['title', 'note','created_time', 'updated_time']

    def create(self, validated_data):
        user = self.context.get('user')
        tag = self.context.get('tag')
        if tag:
            tag, created = models.Tag.objects.get_or_create(title=tag)
            snippet = models.Snippet.objects.create(tag=tag,created_user=user, **validated_data)
            return snippet
        else:
            return models.Snippet.objects.create(created_user=user,**validated_data)