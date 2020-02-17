from django.conf.urls import url
from django.conf import settings
from . import views
from .views import PostView

urlpatterns = [
  url(r'^$', views.PostView.as_view(), name='home'),
  url(r'^api/rating/$', views.RatingList.as_view())
]