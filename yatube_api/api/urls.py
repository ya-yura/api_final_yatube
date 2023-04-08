"""
API URLS
"""

from django.urls import path, include
from rest_framework.routers import SimpleRouter
# from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


app_name = 'api'

router = SimpleRouter()

router.register('posts',
                PostViewSet,
                basename='posts')

router.register('groups',
                GroupViewSet,
                basename='groups')

router.register(r'posts\/(?P<post_id>[^/.]+)\/comments',
                CommentViewSet,
                basename='comments')

router.register('follow',
                FollowViewSet,
                basename='follow')

# YaTube API v.1
v1 = [
    path('', include(router.urls)),

    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(v1)),
]
