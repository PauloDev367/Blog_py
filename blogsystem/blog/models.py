from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        abstract = True

class Category(Base):
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name
    
class Post(Base):
    title = models.CharField(max_length=255)
    post_text = models.TextField()
    main_photo = models.ImageField(upload_to='main-photo/')
    category = models.ManyToManyField(Category, related_name='posts')
    author = models.ForeignKey(User, related_name='author', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title
    
class PostPhoto(Base):
    path = models.ImageField()