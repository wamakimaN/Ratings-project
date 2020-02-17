from django.conf.urls import url
from django.conf import settings
from projects import views
from .views import PostView, PostDetailView
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
  url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  url(r'^logout/$', auth_views.logout, {"next_page": '/'}, name='logout'),
  url(r'^signup/$',views.registration, name='signup'),
  # url(r'^rate/$', views.PostCreate.as_view(), name='rate'),
  url(r'^post/$', views.PostCreate.as_view(), name='post_new'),
  url(r'^$', views.PostView.as_view(), name='home'),
  url(r'^details/(?P<id>[\d]+)/', views.PostDetailView.as_view(), name='details'),
  url(r'^api/rating/$', views.RatingList.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)