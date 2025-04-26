from django.shortcuts import render, redirect
from .models import IBGEFood
from users.views import gerir_contexto


def listar_alimentos(request):
    """
    Exibe a lista de alimentos com opção de busca, para usuários autenticados.
    Funcionalidades:
    Exibe todos os alimentos ordenados alfabeticamente por nome
    Quando o termo de busca contém apenas letras (isalpha())
    Quando o termo de busca contém números ou números e letras (isalnum())

    Args:
        request (HttpRequest): Objeto de requisição Django contendo:
            - Método POST com parâmetro 'search' (opcional)
            - Sessão do usuário para verificação de autenticação

    Returns:
        HttpResponse: Renderiza 'foods/listar_alimentos.html' com:
            - Lista completa de alimentos (ordem alfabética) OU
            - Resultados filtrados por RA (ordem alfabética)
            - Contexto com informações de login
        HttpResponseRedirect: Redireciona para 'index' se usuário não autenticado
    """

    contexto = gerir_contexto(request)
    lista_alimentos = []

    if request.method == 'POST' and contexto['login']:
        search = request.POST.get('search')

        if search.isalpha():
            lista_alimentos = IBGEFood.objects.order_by('descricao_do_alimento').filter(
                descricao_do_alimento__icontains=search)
        elif search.isalnum():
            lista_alimentos = IBGEFood.objects.order_by('descricao_do_alimento').filter(
                codigo__icontains=search)
    else:
        if contexto['login']:
            lista_alimentos = IBGEFood.objects.order_by('descricao_do_alimento').all()
        else:
            return redirect('index')

    contexto['lista_alimentos'] = lista_alimentos
    return render(request, 'foods/listar_alimentos.html', contexto)


