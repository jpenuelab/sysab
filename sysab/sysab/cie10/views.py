from .models import Cie10
from .serializers import Cie10Serializer
from rest_framework import viewsets
# Create your views here.

class CieViewSet(viewsets.ModelViewSet):
    serializer_class = Cie10Serializer
    queryset = Cie10.objects.all()
