from django.shortcuts import render,get_object_or_404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token



def home(request):
    return render(request, 'index.html')

class AllRestaurant(APIView):
    
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, id=None):
        if id:
            restaurant = Restaurant.objects.get(id=id)
            serializer = RestaurantSerializer(restaurant)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)   

    def put(self, request, id=None):
        restaurant = Restaurant.objects.get(id=id)
        serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


    def delete(self, request, id=None):
        restaurant = get_object_or_404(Restaurant, id=id)
        restaurant.delete()
        return Response({"status": "success", "data": "student Deleted"})
    
