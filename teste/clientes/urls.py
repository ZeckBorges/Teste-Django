from django.urls import path
from . import views


urlpatterns = [
    path('clientes/', views.ClienteListCreate.as_view()),
    path('clientes/<int:pk>/', views.ClienteRetrieveUpdateDestroy.as_view())
]
