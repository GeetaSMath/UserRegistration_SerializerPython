import jwt
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    """
    The first part of the serializer class defines the fields
    """
    username = serializers.CharField(required=True, max_length=100)
    password = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    first_name =serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)



    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], email=validated_data['email'],
                                               password=validated_data['password'],first_name=validated_data['first_name'],
                                        last_name=validated_data['last_name'])

        return user


