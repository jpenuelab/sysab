from django.urls import path, include
from .views import CentroViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('centros', CentroViewSet, basename='centros')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
