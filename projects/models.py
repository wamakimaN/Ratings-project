from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  bio = models.TextField(max_length = 30, blank = True)
  profile_pic = models.ImageField(default= 'default.jpg', upload_to='profile_pics')
  


