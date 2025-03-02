from django.db import models

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        abstract = True

class Category(Base):
    name = models.CharField(max_length=255)
    
class Post(Base):
    title = models.CharField(max_length=255)
    post_text = models.TextField()
    main_photo = models.ImageField(upload_to='main-photo/')
    category = models.ManyToManyField(Category, related_name='posts')
    
class PostPhoto(Base):
    path = models.ImageField()