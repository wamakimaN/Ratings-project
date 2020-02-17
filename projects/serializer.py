from rest_framework import serializers
from .models import Post, Rating

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Rating
    fields = ('post','user','stars')