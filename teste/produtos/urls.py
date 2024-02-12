from django.urls import path
from . import views


urlpatterns = [
    path('produtos/', views.ProdutoListCreate.as_view()),
    path('produtos/<int:pk>/', views.ProdutoRetrieveUpdateDestroy.as_view()),
]