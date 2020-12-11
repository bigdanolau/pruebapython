from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
    )
from .models import Pregunta
from .serializers import PersonSerializer
class HomeView(TemplateView):
    template_name = "home/home.html"

# Create your views here.

class PreguntasListApiView(ListAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return Pregunta.objects.all()
    
class PreguntasCreateView(CreateAPIView):
    serializer_class = PersonSerializer
   
    


class PreguntasRetrieveView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Pregunta.objects.filter()
  
class PreguntasDELETEView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Pregunta.objects.filter()
  
class PreguntasUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Pregunta.objects.filter()
  

