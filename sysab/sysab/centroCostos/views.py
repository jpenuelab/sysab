from .models import TbCentroCostos
from .serializers import CentroSerializer
from rest_framework import viewsets

class CentroViewSet(viewsets.ModelViewSet):
    serializer_class = CentroSerializer
    queryset = TbCentroCostos.objects.all()