from django.contrib import admin
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    path("inicio",views.HomeView.as_view()),
    path("api/v1/preguntas/list",views.PreguntasListApiView.as_view()),
    path("api/v1/preguntas/create",views.PreguntasCreateView.as_view()),
    path("api/v1/preguntas/detail/<pk>",views.PreguntasRetrieveView.as_view()),
    path("api/v1/preguntas/delete/<pk>",views.PreguntasDELETEView.as_view()),
    path("api/v1/preguntas/update/<pk>",views.PreguntasUpdateView.as_view())

]
