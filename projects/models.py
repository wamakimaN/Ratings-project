from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  bio = models.TextField(max_length = 100, blank = True)
  profile_pic = models.ImageField(default= 'default.jpg', upload_to='profile_pics')
  
  def __str__(self):
    return f'{self.user.username} Profile'


class Post(models.Model):
  profile = models.ForeignKey(Profile, null = True, blank = True)
  name = models.CharField(max_length = 60)
  image = models.ImageField(upload_to='post_pics')
  site = models.URLField(max_length = 60)
  posted_on = models.DateTimeField(auto_now_add=True,null = True)
  description = models.TextField(max_length = 200)

  def __str__(self):
    return self.name

class Rating(models.Model):
  post = models.ForeignKey(Post, on_delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  remark = models.TextField(max_length = 200,blank = True)
  stars = models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])