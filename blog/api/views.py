from .serializers import BlogPostSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from blog.models import BlogPost


class BlogListAPIView(generics.ListAPIView):
    lookup_field = 'pk'
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAdminUser]