from dataclasses import field
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password

class RestaurantSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Restaurant
        fields = '__all__'