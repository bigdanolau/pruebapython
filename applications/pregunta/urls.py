from django.contrib import admin
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path("inicio",views.HomeView.as_view()),
    path("api/v1/preguntas/listado",views.PreguntasListApiView.as_view())

]
