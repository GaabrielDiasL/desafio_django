from rest_framework import generics
from .models import Esporte, Time
from .serializers import EsporteSerializer, TimeSerializer

class TimeList(generics.ListCreateAPIView):
    serializer_class = TimeSerializer

    def get_queryset(self):
        queryset = Time.objects.all()
        esporte = self.request.query_params.get('esporte')
        if esporte is not None:
            queryset = queryset.filter(esporte_nome = esporte)
        return queryset
    
class TimeDetail(generics.RetrieveDestroyAPIView):
    serializer_class = TimeSerializer
    queryset = Time.objects.all()

class EsporteList(generics.ListCreateAPIView):
    serializer_class = EsporteSerializer
    queryset = Esporte.objects.all()

class EsporteDetail(generics.RetrieveDestroyAPIView):
    serializer_class = EsporteSerializer
    queryset = Esporte.objects.all()
