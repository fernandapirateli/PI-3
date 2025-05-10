from django.shortcuts import render, redirect
from .models import IBGEFood
from users.views import gerir_contexto
from django.db.models import Q
from .class_food import *
from .class_nutrition import *


GLOBAL_LIST_FOOD_ID = []


def pesquisar_alimentos(request):
    """
    Realiza uma busca flexível por alimentos no banco de dados IBGE com filtros opcionais.

    Args:
        request (HttpRequest): Objeto de requisição Django contendo os parâmetros POST:
            - search (str): Termo de busca obrigatório (pode ser nome ou código)
            - categoria (str, optional): Filtro por categoria de alimento
            - modo_preparo (str, optional): Filtro por código de preparo
    Returns:
        QuerySet: Lista de objetos IBGEFood ordenados alfabeticamente por descrição, filtrados por:
            - Termo de busca (no nome OU código)
            - Categoria (se fornecida)
            - Modo de preparo (se fornecido)
    """

    lista_alimentos = []
    search = request.POST.get('search')
    categoria = request.POST.get('categoria')
    cod_preparo = request.POST.get('modo_preparo')

    food_query = Q(descricao_do_alimento__icontains=search)
    if categoria is not None:
        food_query &= Q(categoria=categoria)
    if cod_preparo is not None:
        food_query &= Q(codigo_de_preparacao=cod_preparo)

    if search.isalpha():
        lista_alimentos = IBGEFood.objects.order_by('descricao_do_alimento').filter(food_query)
    elif search.isalnum():
        lista_alimentos = IBGEFood.objects.order_by('descricao_do_alimento').filter(
            codigo__icontains=search)

    return lista_alimentos


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
            - Resultados filtrados por Código (ordem alfabética)
            - Contexto com informações de login
        HttpResponseRedirect: Redireciona para 'index' se usuário não autenticado
    """

    contexto = gerir_contexto(request)
    if request.method == 'POST' and contexto['login']:
        lista_alimentos = pesquisar_alimentos(request)
    else:
        if contexto['login']:
            lista_alimentos = IBGEFood.objects.order_by('descricao_do_alimento').all()
        else:
            return redirect('index')

    contexto['lista_alimentos'] = lista_alimentos
    return render(request, 'foods/listar_alimentos.html', contexto)


def somar_alimentos(request):
    """
    Gerencia a lista global de alimentos selecionados e calcula seus valores nutricionais totais,
    comparando com as necessidades diárias por faixa etária.

    Args:
        request (HttpRequest): Objeto de requisição Django contendo:
            - option (str, optional): Define a ação ('inserir' ou 'remover')
            - food_id (str, optional): ID do alimento para inserção
            - remove_food_ids (list, optional): IDs dos alimentos para remoção
    Returns:
        HttpResponse: Renderiza 'foods/somar_alimentos.html' com:
            - Lista de alimentos selecionados
            - Totais nutricionais calculados
            - Porcentagens das necessidades diárias
            - Dicas nutricionais para a faixa etária
        HttpResponseRedirect: Redireciona para 'index' se usuário não autenticado
    """

    global GLOBAL_LIST_FOOD_ID

    lista_alimentos = []
    lista_faixas_etarias = ['4-8_anos', '9-13_anos', '14-18_anos']
    faixa_etaria = lista_faixas_etarias[1]
    contexto = gerir_contexto(request)

    if contexto['login']:
        option = request.POST.get('option')

        if request.method == 'POST' and option is None:
            lista_alimentos = pesquisar_alimentos(request)

        if request.method == 'POST' and option == 'inserir':
            food_id = request.POST.get('food_id')
            GLOBAL_LIST_FOOD_ID.append(food_id)

        if request.method == 'POST' and option == 'remover':
            remove_food_ids = request.POST.getlist('remove_food_ids')
            if len(remove_food_ids) > 0:
                [GLOBAL_LIST_FOOD_ID.remove(food_id) for food_id in remove_food_ids]
            else:
                pass

        list_objects = IBGEFood.objects.filter(pk__in=GLOBAL_LIST_FOOD_ID)
        dict_total = calcular_nutrientes(list_objects)

        dict_daily_value = DRIS_NUTRICIONAIS[faixa_etaria]
        dict_pct = calcular_pct(dict_daily_value, dict_total)

        contexto['tips'] = OBSERVACAO[faixa_etaria]
        contexto['dict_pct'] = dict_pct
        contexto['dict_total'] = dict_total
        contexto['list_objects'] = list_objects
        contexto['lista_alimentos'] = lista_alimentos
        contexto['modo_preparo_choices'] = MODO_PREPARO
        contexto['categoria_choices'] = CATEGORIA

        return render(request, 'foods/somar_alimentos.html', contexto)

    else:
        return redirect('index')


def detalhes_alimento(request):
    """
    Exibe o detalhes de um alimento específico quando acessado via POST.
    Recupera os dados do alimento com base no ID fornecido e renderiza a página
    de detalhes com essas informações. Acesso restrito via método POST.

    Args:
        request (HttpRequest): Objeto de requisição contendo:
            - POST: food_id (ID do alimento a ser visualizado)
    Returns:
        HttpResponse: Renderiza 'foods/detalhes_alimento.html' com os dados do alimento
        HttpResponseRedirect: Redireciona para 'index' se acessado via GET
    """

    if request.method == 'POST':
        contexto = gerir_contexto(request)
        food_id = request.POST.get('food_id')
        contexto['food'] = IBGEFood.objects.get(pk=food_id)
        return render(request, 'foods/detalhes_alimento.html', contexto)

    else:
        return redirect('index')


def calcular_nutrientes(list_objects):
    """
    Calcula os valores nutricionais totais para uma lista de alimentos, somando os macronutrientes.

    Args:
        list_objects (QuerySet): Lista de objetos IBGEFood para cálculo nutricional
    Returns:
        dict: Dicionário com:
            - Chaves: Nomes dos campos de macronutrientes (ex: 'proteina_g')
            - Valores: Listas contendo:
                [0]: Soma total do nutriente (float)
                [1]: Nome amigável do nutriente (str, primeira palavra do verbose_name)
    """

    dict_total = {}
    grams = 100

    for nutriente, verbose in MACRONUTRIENTES:
        verbose = verbose.split()[0]
        dict_total[nutriente] = [0.0, verbose]

    for food in list_objects:
        factor = grams / 100
        for key in dict_total.keys():

            valor_nutriente = getattr(food, key, 0.0)
            valor_nutriente = 0.0 if valor_nutriente is None else valor_nutriente
            dict_total[key][0] += float(valor_nutriente) * factor

    return dict_total


def calcular_pct(dict_daily_value, dict_current):
    """
    Calcula a porcentagem de atendimento das necessidades diárias nutricionais.

    Args:
        dict_daily_value (dict): Valores diários recomendados (DRIs) para cada nutriente
        dict_current (dict): Valores atuais consumidos para cada nutriente (formato: {nutriente: [valor, verbose]})
    Returns:
        dict: Dicionário com:
            - Chaves: Nomes dos campos de nutrientes (ex: 'proteina_g')
            - Valores: Porcentagem (float) do valor diário recomendado (arredondado para 1 decimal)
    """

    dict_pct = {}
    dict_correcao = {
        'fibras_g': 'fibra_alimentar_total_g',
        'proteinas_g': 'proteina_g',
        'carboidratos_g': 'carboidrato_g'
    }
    for macro_nutri, valor_nutriente in dict_daily_value.items():
        macro_nutri = dict_correcao[macro_nutri] if macro_nutri in dict_correcao.keys() else macro_nutri
        dict_pct[macro_nutri] = round((dict_current[macro_nutri][0] * 100) / valor_nutriente, 1)

    return dict_pct
