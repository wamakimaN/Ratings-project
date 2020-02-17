from django.shortcuts import render, get_object_or_404,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
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

class PostDetailView(DetailView):
  template_name = 'details.html'
  queryset = Post.objects.all()

  def get_object(self):
    id_ = self.kwargs.get("id") 
    return get_object_or_404(Post, id=id_)

class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'new_post.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'new_post.html', {'form': form})

def registration(request):
  form = UserCreationForm()

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()

  context = {'form':form}
  return render(request, 'signup.html', context)
