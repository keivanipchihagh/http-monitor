from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'username', 'password', 'email')
        extra_kwargs = { 'password': {'write_only': True} }


    def validate(self, attrs):
        return super().validate(attrs)


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


    def update(self, instance, validated_data):
        return super().update(instance, validated_data)