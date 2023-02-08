from rest_framework import serializers
from ..models import Blog


class BlogSerializer(serializers.ModelSerializer):
    author = user = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all(), many=False)
    title_image = serializers.ImageField(required=False)

    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'author',
            'description',
            'title_image',
        ]
