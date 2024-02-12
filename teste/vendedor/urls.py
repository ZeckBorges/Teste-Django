from django.urls import path
from . import views


urlpatterns = [
    path('vendedor/', views.VendedorListCreate.as_view()),
    path('vendedor/<int:pk>/', views.VendedorRetrieveUpdateDestroy.as_view()),
]