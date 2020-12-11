from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
    )
from .models import Respuesta
from .serializers import RespuestaSerializer

# Create your views here.

class RespuestasListApiView(ListAPIView):
    serializer_class = RespuestaSerializer
    def get_queryset(self):
        return Respuesta.objects.all()
    
class RespuestasCreateView(CreateAPIView):
    serializer_class = RespuestaSerializer
   
    #hk


class RespuestasRetrieveView(RetrieveAPIView):
    serializer_class = RespuestaSerializer
    queryset = Respuesta.objects.filter()
  
class RespuestasDELETEView(DestroyAPIView):
    serializer_class = RespuestaSerializer
    queryset = Respuesta.objects.filter()
  
class RespuestasUpdateView(RetrieveUpdateAPIView):
    serializer_class = RespuestaSerializer
    queryset = Respuesta.objects.filter()
  
