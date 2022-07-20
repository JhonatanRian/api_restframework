from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True},
            'password': {'write_only': True},
        }
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password'
        )