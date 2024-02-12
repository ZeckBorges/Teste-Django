from django.urls import path
from . import views

urlpatterns = [
    path('vendas/', views.VendaListCreate.as_view()),
    path('vendas/<int:pk>/', views.VendaRetrieveUpdateDestroy.as_view()),
]
