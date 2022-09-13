from rest_framework import viewsets, generics
from cliente.serializer import ClienteSerializer
from cliente.models import Cliente


class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    http_method_names = ['get', 'post', 'put']


class ListaCliente(generics.ListAPIView):
    def get_queryset(self):
        queryset = Cliente.objects.all
        return queryset
    serializer_class = ClienteSerializer


