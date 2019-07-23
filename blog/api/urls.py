from django.conf.urls import url
from .views import BlogListAPIView

app_name = 'api'

urlpatterns = [
    url(r'^$', BlogListAPIView.as_view(), name='blog-list')
]