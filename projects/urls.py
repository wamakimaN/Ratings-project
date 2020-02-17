from django.conf.urls import url
from django.conf import settings
from . import views
from .views import PostView, PostDetailView
from django.conf.urls.static import static

urlpatterns = [
  url(r'^$', views.PostView.as_view(), name='home'),
  url(r'^details/(?P<id>[\d]+)/', views.PostDetailView.as_view(), name='details'),
  url(r'^api/rating/$', views.RatingList.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)