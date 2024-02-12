from rest_framework import generics
from .models import Vendedor
from .serializers import VendedorSerializer

class VendedorListCreate(generics.ListCreateAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class VendedorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
