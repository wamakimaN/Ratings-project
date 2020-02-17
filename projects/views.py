from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Rating
from .serializer import RatingSerializer


# Create your views here.
class RatingList(APIView):
  def get(self, request, formal=None):
    ratings = Rating.objects.all()
    serializers = RatingSerializer(ratings, many=True)
    return Response(serializers.data)