from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, EmailField, CharField, ValidationError
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class RegisterSerializer(ModelSerializer):
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = CharField(
        write_only=True, required=True, validators=[validate_password])

    password_confirmation = CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password',  # Include password field
            'password_confirmation'  # Include password_confirmation field
        )
        extra_kwargs = {
            'password_confirmation': {'required': True},
        }

    def validate(self, validated_data):
        password = validated_data.get('password')  # Extract and remove password from validated_data
        password_confirmation = validated_data.get(
            'password_confirmation')  # Extract and remove password_confirmation from validated_data

        if password != password_confirmation:
            raise ValidationError('Passwords do not match')

        return validated_data

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(password)  # Set the user's password securely
        user.save()
        return user
