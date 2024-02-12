from django.urls import path
from . import views


urlpatterns = [
    path('grupoproduto/', views.GrupoProdutoListCreate.as_view()),
    path('grupoproduto/<int:pk>/', views.GrupoProdutoRetrieveUpdateDestroy.as_view()),
]