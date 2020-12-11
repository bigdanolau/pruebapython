from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("api/v1/respuesta/list",views.RespuestasListApiView.as_view()),
    path("api/v1/respuesta/create",views.RespuestasCreateView.as_view()),
    path("api/v1/respuesta/detail/<pk>",views.RespuestasRetrieveView.as_view()),
    path("api/v1/respuesta/delete/<pk>",views.RespuestasDELETEView.as_view()),
    path("api/v1/respuesta/update/<pk>",views.RespuestasUpdateView.as_view())
]
