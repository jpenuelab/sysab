from rest_framework import serializers
from .models import TbEps


class TbEpsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TbEps
        # fields = ['nombre_eps','estado']
        fields = '__all__'


    


