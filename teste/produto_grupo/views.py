from rest_framework import generics
from .models import GrupoProduto
from .serializers import GrupoProdutoSerializer

class GrupoProdutoListCreate(generics.ListCreateAPIView):
    queryset = GrupoProduto.objects.all()
    serializer_class = GrupoProdutoSerializer

class GrupoProdutoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = GrupoProduto.objects.all()
    serializer_class = GrupoProdutoSerializer
