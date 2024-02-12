from django.urls import path
from . import views


urlpatterns = [
    path('itens/', views.ItemVendaListCreate.as_view()),
]
