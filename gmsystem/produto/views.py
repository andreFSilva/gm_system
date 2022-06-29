from django.views.generic import ListView

from .models import Produto


class ProdutoListView(ListView):
    model = Produto
    template_name = "produto/produto_list.html"
    context_object_name = "produtos"

    def get_queryset(self):
        return Produto.objects.all()
