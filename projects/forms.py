from django import forms
from .models import Post, Profile, Rating

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['profile','posted_on']

class RateForm(forms.ModelForm):
  class Meta:
    model = Rating
    exclude = ['user','post']
