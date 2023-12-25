from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("busqueda/", views.resultado_busqueda, name="resultado_busqueda"),
    path("categoria/<str:categoria>", views.categorias, name="categorias"),
    path("nuevo_producto/", views.crear_producto, name="crear_producto"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
