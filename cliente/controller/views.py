from rest_framework import viewsets, generics
from cliente.servicer.serializer import ClienteSerializer
from cliente.models.models import Cliente


class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    http_method_names = ['get', 'post', 'put', 'delete']


class ListaCliente(generics.ListAPIView):
    def get_queryset(self):
        queryset = Cliente.objects.all
        return queryset
    serializer_class = ClienteSerializer


