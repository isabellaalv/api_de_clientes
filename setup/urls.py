from django.contrib import admin
from django.urls import path,include
from cliente.controller.views import ClienteViewSet, ListaCliente
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cliente', ClienteViewSet, basename='cliente')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/', ListaCliente.as_view()),

]
