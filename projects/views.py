from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.list import ListView
from .models import  Rating, Post
from .serializer import RatingSerializer
from rest_framework import status


# Create your views here.
class PostView(ListView):
  template_name = 'home.html'
  queryset = Post.objects.all()

class RatingList(APIView):
  def get(self, request, formal=None):
    ratings = Rating.objects.all()
    serializers = RatingSerializer(ratings, many=True)
    return Response(serializers.data)

  def post(self, request, format = None):
    serializers = RatingSerializer(data=request.data)
    if serializers.is_valid():
      serializers.save()
      return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)