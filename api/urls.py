from django.urls import path
from .views import EsporteList, EsporteDetail, TimeList, TimeDetail

urlpatterns = [
    path('time/', TimeList.as_view()),
    path('time/<int:pk>', TimeDetail.as_view()),
    path('esporte/', EsporteList.as_view()),
    path('esporte/<int:pk>', EsporteDetail.as_view()),
]