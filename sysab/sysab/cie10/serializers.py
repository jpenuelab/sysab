from .models import Cie10
from rest_framework import serializers

class Cie10Serializer(serializers.ModelSerializer):

    class Meta:
        model = Cie10
        fields = '__all__'