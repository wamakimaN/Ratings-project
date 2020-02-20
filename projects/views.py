from django.shortcuts import render, get_object_or_404,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import ListView, DetailView, FormView
from django.views import View
from .forms import PostForm, RateForm
from django.contrib.auth.forms import UserCreationForm
from .models import  Rating, Post
from .serializer import RatingSerializer
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

class PostDetail(DetailView):
  template_name = 'details.html'
  model = Post

  def get_object(self):
    object = super(PostDetail,self).get_object()
    return object

  def get_context_data(self, **kwargs):
    context = super(PostDetail, self).get_context_data(**kwargs)
    context['ratings'] = Rating.objects.filter(post=self.get_object())
    context['form'] = RateForm
    return context

class PostRating(FormView):
  form_class = RateForm
  template_name = 'details.html'

  def form_valid(self,form):
    form.instance.profile.user = self.request.user


@method_decorator(login_required, name='dispatch')
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

@method_decorator(login_required, name='dispatch')
class RatePost(View):
    def get(self, request):
        form = RateForm()
        return render(request, 'rate.html', {'form': form})

    def post(self, request):
        form = RateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'rate.html', {'form': form})

def registration(request):
  form = UserCreationForm()

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()

  context = {'form':form}
  return render(request, 'signup.html', context)