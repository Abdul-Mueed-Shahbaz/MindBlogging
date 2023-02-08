from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            # "staff",
            # "admin",
            "email",

        ]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # password = serializers.CharField(
    #     write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name'
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        # user.set_password(validated_data['password'])
        # user.set_unusable_password()
        user.save()
        return user
