from django.shortcuts import render, get_object_or_404
from galeria.models import Produto
#from django.http import HttpResponse

#produtos = {
#    1: {"nome_produto": "toddynho",
#        "preco": 5.99,
#        "quantidade": 10, },
#        
#    2: {"nome_produto": "toddynho",
#        "preco": 5.99,
#        "quantidade": 10, }
#}

produtos = Produto.objects.all()

def index(request):
    #return HttpResponse("Olá, Mundo!")
    #return render(request, 'index.html', {"produtos": produtos})
    return render(request, 'index.html', {"produtos": produtos})

def teste(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'teste.html', {'produto': produto})