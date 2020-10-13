
from django.urls import path, include
# from .views import eps_list, eps_detail
from .views import EpsAPIView, EpsDetails, GenericAPIView, EpsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('eps', EpsViewSet, basename='eps')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    # path('', eps_list),
    path('', EpsAPIView.as_view()),
    # path('<int:pk>/', eps_detail)
    path('<int:id_eps>/', EpsDetails.as_view()),
    path('generic/', GenericAPIView.as_view()),
    path('generic/<int:id_eps>/', GenericAPIView.as_view()),
]