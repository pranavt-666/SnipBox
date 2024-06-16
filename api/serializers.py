from rest_framework import serializers
from api import models


class TagSerializer(serializers.Serializer):
    title = serializers.CharField()


class SnippetSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(read_only=True)
    updated_time = serializers.DateTimeField(read_only=True)
    created_user = serializers.CharField(read_only=True)
    tag = serializers.CharField(read_only=True)

    class Meta:
        model = models.Snippet
        fields = '__all__'