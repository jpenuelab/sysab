from rest_framework import serializers
from .models import TbCentroCostos

class CentroSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbCentroCostos
        fields = '__all__'
        