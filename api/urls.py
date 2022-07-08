from django.urls import path, include
from rest_framework import routers
from .views import TrackViewSet

router = routers.DefaultRouter()

router.register(r'tracks', TrackViewSet)


urlpatterns = [
    path('contents/', include(router.urls)),
]
