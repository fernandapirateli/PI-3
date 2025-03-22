from django.shortcuts import render, redirect
from django.contrib import auth

User = auth.get_user_model()
GLOBAL_LOGIN = False


def gerir_contexto(request):
    global GLOBAL_LOGIN

    contexto = {'login': GLOBAL_LOGIN}
    if request.user.is_authenticated:
        contexto['first_name'] = request.user.first_name
        contexto['user_type'] = request.user.user_type
    return contexto


def index(request):
    contexto = gerir_contexto(request)
    return render(request, 'index.html', contexto)


def perfil(request):
    contexto = gerir_contexto(request)
    if contexto['login']:
        return render(request, 'users/profile.html', contexto)
    else:
        return redirect('index', contexto)


def registrar(request):
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


def logout(request):
    global GLOBAL_LOGIN

    auth.logout(request)
    GLOBAL_LOGIN = False
    contexto = {'login': GLOBAL_LOGIN}
    return render(request, 'index.html', contexto)
