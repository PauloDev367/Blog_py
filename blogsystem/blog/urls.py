from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import CategoryViewSet, PostPhotoViewSet, PostViewSet, LoginView, RegisterView

router = SimpleRouter()
router.register('categories', CategoryViewSet)
router.register('posts', PostViewSet)
router.register('postphotos', PostPhotoViewSet)

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
]