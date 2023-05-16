from rest_framework import serializers
from .models import Time, Esporte

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('__all__')

class EsporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esporte
        fields = ('__all__')