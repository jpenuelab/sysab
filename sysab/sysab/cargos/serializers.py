from rest_framework import serializers
from .models import TbCargos

class CargosSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbCargos
        fields = '__all__'

