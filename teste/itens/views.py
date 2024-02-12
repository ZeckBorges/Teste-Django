from rest_framework import generics
from .models import ItemVenda
from .serializers import ItemVendaSerializer

class ItemVendaListCreate(generics.ListCreateAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer

class ItemVendaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemVenda.objects.all()
    serializer_class = ItemVendaSerializer
