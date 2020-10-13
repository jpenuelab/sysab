from .models import TbEmpleado
from .serializers import EmpleadoSerializer
from rest_framework import viewsets

# Create your views here.

class EmpleadoViewSet(viewsets.ModelViewSet):

    serializer_class = EmpleadoSerializer
    queryset = TbEmpleado.objects.all()