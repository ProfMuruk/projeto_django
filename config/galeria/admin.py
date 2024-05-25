from django.contrib import admin
from galeria.models import Produto

class ListarProdutos(admin.ModelAdmin):
    list_display = ("id", "nome_produto", "quantidade", "preco")
    list_display_links = ("id", "nome_produto")
    search_fields = ("nome_produto",)

admin.site.register(Produto, ListarProdutos)
