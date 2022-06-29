from django.contrib import admin

from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "preco",
        "estoque",
        "disponivel",
        "data_criacao",
        "data_atualizacao",
    )
    list_filter = ("nome", "estoque", "disponivel", "data_criacao", "data_atualizacao")
    search_fields = ("nome", "descricao")
    ordering = ("nome",)
