from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse

User = auth.get_user_model()


def index(request):
    contexto = {'login': False}
    if request.user.is_authenticated:
        contexto = {
            'first_name': request.user.first_name,
            'user_type': request.user.user_type,
            'login': True,
        }
    return render(request, 'index.html', contexto)


def perfil(request):
    if request.user.is_authenticated:
        return render(request, 'users/profile.html')
    else:
        return HttpResponse(status=400)


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
        return render(request, 'registrar.html')


def logar(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        password = request.POST.get('password')

        if User.objects.filter(username=cpf).exists():
            user = auth.authenticate(request, username=cpf, password=password)

            if user is not None:
                auth.login(request, user)
                print(f'Usuário {user.first_name} logado.')
                return redirect('index')
        else:
            print('CPF ou senha inválidos')
    return render(request, 'logar.html')


def logout(request):
    auth.logout(request)
    contexto = {'login': False}
    return render(request, 'index.html', contexto)
