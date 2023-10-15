from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import Blog


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), many=False, required=False)
    title_image = serializers.ImageField(required=False)

    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'author',
            'description',
            'title_image',
            'content',
        ]
