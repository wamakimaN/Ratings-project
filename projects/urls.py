from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^api/rating/$', views.RatingList.as_view())
]