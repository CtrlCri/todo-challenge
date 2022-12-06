from rest_framework import routers
from .api import TodolistViewSet

router = routers.DefaultRouter()

router.register('api/todolist', TodolistViewSet, 'todolist')

urlpatterns = router.urls