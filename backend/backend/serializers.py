from rest_framework import serializers
from django.contrib.auth.models import User

from backend.models import Application, Job

class RegisterSerializer(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['username', 'email', 'password']

class Jobserializer(serializers.ModelSerializer):
     created_by = serializers.StringRelatedField()

     class Meta:
          model =Job
          fields= "__all__"

class Applicationserializer(serializers.ModelSerializer):
     class Meta:
         model= Application
         fields = "__all__" 
