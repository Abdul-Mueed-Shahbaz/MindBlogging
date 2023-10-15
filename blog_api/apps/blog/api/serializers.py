from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, ImageField
from ..models import Blog


class BlogSerializer(ModelSerializer):
    author = PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), many=False, required=False)
    title_image = ImageField(required=False)

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
