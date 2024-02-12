from rest_framework import generics
from .models import Venda
from .serializers import VendaSerializer

class VendaListCreate(generics.ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer