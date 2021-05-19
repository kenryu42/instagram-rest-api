from rest_framework import routers
from .views import UserViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('posts', PostViewSet)