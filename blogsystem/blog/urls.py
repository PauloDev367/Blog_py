from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, PostPhotoViewSet, PostViewSet

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('posts', PostViewSet)
router.register('postphotos', PostPhotoViewSet)