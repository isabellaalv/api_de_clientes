from django.contrib import admin

from cliente.models.models import Cliente


class cliente(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'data_nascimento', 'ultima_compra', 'endereco', 'foto')
    list_display_links = ('id', 'nome', 'cpf', 'data_nascimento', 'ultima_compra', 'endereco', 'foto')
    search_fields = ('nome', 'id')
    list_per_page = 50


admin.site.register(Cliente, cliente)
