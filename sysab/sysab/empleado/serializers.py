from rest_framework import serializers
from .models import TbEmpleado

class EmpleadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TbEmpleado
        fields = '__all__'