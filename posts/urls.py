from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from . import views
from .views import FeedView,LikePostView, UnlikePostView

# Create a router and register viewsets
router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)

# URL patterns
urlpatterns = [ path('feed/', FeedView.as_view(), name='feed'), path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),] + router.urls
