from rest_framework import serializers
from .models import Category, Post, PostPhoto


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'post_text',
            'main_photo',
            'category'
        )
class PostPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhoto
        fields = ('id', 'path')