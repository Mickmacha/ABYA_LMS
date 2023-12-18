from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)  # print validated data
        password = validated_data.pop('password')
        user = get_user_model().objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user