from django.shortcuts import render, redirect
from django.contrib import auth
import users.analytics as an

User = auth.get_user_model()
GLOBAL_LOGIN = False


def gerir_contexto(request):
    """
    Gera um dicionário de contexto padrão para as views.
    Adiciona informações de login globais e, se o usuário estiver autenticado,
    inclui o primeiro nome e tipo de usuário.

    Args:
        request (HttpRequest): Objeto de requisição Django contendo informações do usuário.
    Returns:
        dict: Dicionário contendo:
            - login: Valor da variável global GLOBAL_LOGIN
            - first_name: Primeiro nome do usuário (apenas se autenticado)
            - user_type: Tipo do usuário (apenas se autenticado)
    """

    global GLOBAL_LOGIN

    contexto = {'login': GLOBAL_LOGIN}
    if request.user.is_authenticated:
        contexto['first_name'] = request.user.first_name
        contexto['user_type'] = request.user.user_type
    return contexto


def index(request):
    """
    Renderiza a página inicial do sistema.
    Utiliza o contexto gerado por `gerir_contexto` para fornecer informações
    básicas ao template.

    Args:
        request (HttpRequest): Objeto de requisição Django.
    Returns:
        HttpResponse: Resposta renderizada com o template 'index.html' e o contexto.
    """

    contexto = gerir_contexto(request)
    return render(request, 'index.html', contexto)


def perfil(request):
    """
    Renderiza a página de perfil do usuário se autenticado, ou redireciona para a página inicial.
    Verifica no contexto se há um login ativo para decidir entre mostrar o perfil
    ou redirecionar. Utiliza o contexto gerado por `gerir_contexto`.

    Args:
        request (HttpRequest): Objeto de requisição Django.
    Returns:
        HttpResponse: Resposta renderizada com o template 'users/profile.html' se autenticado,
                     ou redirecionamento para 'index' caso contrário.
    """

    contexto = gerir_contexto(request)
    if contexto['login']:
        return render(request, 'users/profile.html', contexto)
    else:
        return redirect('index', contexto)


def registrar(request):
    """
    Processa o cadastro de novos usuários ou exibe o formulário de registro.
    Para requisições POST:
    - Valida se o CPF já está cadastrado
    - Cria um novo usuário com os dados fornecidos
    - Redireciona para a página de login após cadastro bem-sucedido
    Para requisições GET:
    - Exibe o formulário de registro vazio

    Args:
        request (HttpRequest): Objeto de requisição Django, contendo:
            - POST: first_name, cpf, user_type e password
            - GET: nenhum dado específico
    Returns:
        HttpResponseRedirect: Redireciona para 'registrar' (em caso de CPF existente) ou 'logar' (sucesso)
        HttpResponse: Renderiza 'users/registrar.html' para método GET
    """

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        cpf = request.POST.get('cpf')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')

        if User.objects.filter(username=cpf).exists():
            print('CPF informado já está em uso')
            return redirect('registrar')
        else:
            user = User.objects.create_user(
                username=cpf,
                first_name=first_name,
                password=password,
                user_type=user_type
            )
            user.save()
            print(f'Usuário(a) {first_name} cadastrado(a) com sucesso')
            return redirect('logar')
    else:
        return render(request, 'users/registrar.html')


def logar(request):
    """
    Processa o login de usuários ou exibe o formulário de autenticação.
    Para requisições POST:
    - Verifica as credenciais (CPF e senha)
    - Autentica o usuário se válido
    - Atualiza a variável global GLOBAL_LOGIN
    - Redireciona para a página inicial após login bem-sucedido
    Para requisições GET:
    - Exibe o formulário de login

    Args:
        request (HttpRequest): Objeto de requisição Django contendo:
            - POST: cpf e password
            - GET: nenhum dado específico
    Returns:
        HttpResponseRedirect: Redireciona para 'index' em caso de login bem-sucedido
        HttpResponse: Renderiza 'users/logar.html' para método GET ou credenciais inválidas
    """

    global GLOBAL_LOGIN

    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')

        if User.objects.filter(username=cpf).exists():
            user = auth.authenticate(request, username=cpf, password=password)

            if user is not None:
                auth.login(request, user)
                GLOBAL_LOGIN = True
                print(f'Usuário {user.first_name} logado.')
                return redirect('index')
        else:
            print('CPF ou senha inválidos')
    return render(request, 'users/logar.html')


def deslogar(request):
    """
    Realiza o logout do usuário atual e atualiza o estado de login global.
    Efetua o logout através do sistema de autenticação do Django, desativa a flag
    GLOBAL_LOGIN e renderiza a página inicial com o contexto atualizado.

    Args:
        request (HttpRequest): Objeto de requisição Django contendo a sessão do usuário.
    Returns:
        HttpResponse: Resposta renderizada com o template 'index.html' contendo
                     contexto com estado de login atualizado.
    """

    global GLOBAL_LOGIN

    auth.logout(request)
    GLOBAL_LOGIN = False
    contexto = {'login': GLOBAL_LOGIN}
    return render(request, 'index.html', contexto)


def relatorio_alunos(request):
    contexto = gerir_contexto(request)

    df = an.obter_dataframe()

    # Gera gráfico e relatório
    imagem_barras, relatorio_barras = an.grafico_barras(df)

    contexto['grafico_barras'] = imagem_barras
    contexto['relatorio_barras'] = relatorio_barras

    return render(request, 'users/relatorio_alunos.html', contexto)
