from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("consulta1", views.primera_consulta, name="consulta1"),
    path("consulta2", views.segunda_consulta, name="consulta2"),
    path("consulta3", views.tercera_consulta, name="consulta3"),
    path("consulta4", views.cuarta_consulta, name="consulta4"),
    path("consulta5", views.quinta_consulta, name="consulta5"),
    path("consulta6", views.sexta_consulta, name="consulta6"),
]
