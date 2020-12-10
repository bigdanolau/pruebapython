from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from rest_framework.generics import ListAPIView
from .models import Pregunta
from .serializers import PersonSerializer
class HomeView(TemplateView):
    template_name = "home/home.html"

# Create your views here.

class PreguntasListApiView(ListAPIView):
    serializer_class = PersonSerializer
    def get_queryset(self):
        return Pregunta.objects.all()
    

