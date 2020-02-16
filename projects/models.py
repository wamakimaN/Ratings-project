from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  bio = models.TextField(max_length = 30, blank = True)
  profile_pic = models.ImageField(default= 'default.jpg', upload_to='profile_pics')

class Post(models.Model):
  profile = models.ForeignKey(Profile, null = True, blank = True)
  name = models.CharField(max_length = 60)
  image = models.ImageField(upload_to='post_pics')
  site = models.URLField(max_length = 60)
  description = TextField(max_length = 200)

class Rating(models.Model):
  post = ForeignKey(Post, on_delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  stars = models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])