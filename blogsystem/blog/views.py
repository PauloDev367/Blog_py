from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, PostPhotoSerializer, PostSerializer
from .models import Category, Post, PostPhoto


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class PostPhotoViewSet(viewsets.ModelViewSet):
    queryset = PostPhoto.objects.all()
    serializer_class = PostPhotoSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer