from django.urls import path, include
# from .views import eps_list, eps_detail
from .views import CargosViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cargos', CargosViewSet, basename='cargos')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]