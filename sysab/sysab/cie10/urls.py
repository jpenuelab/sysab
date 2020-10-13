from django.urls import path, include
from .views import CieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cie', CieViewSet, basename='cie')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
