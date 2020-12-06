from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import ModelField

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'