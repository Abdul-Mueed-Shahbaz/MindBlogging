from rest_framework.serializers import ModelSerializer, ImageField, ValidationError

from ..models import Comments


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'id',
            'content',
            'image',
            'blog',
            'user',
        ]

    def validate(self, attrs):
        if not ('image' in attrs or 'content' in attrs):
            raise ValidationError('Blank Comment is not allowed')
        return attrs
