from django.shortcuts import render, redirect
from django.contrib import auth

User = auth.get_user_model()


def index(request):
    if request.user.is_authenticated:
        contexto = {
            'first_name': request.user.first_name,
            'user_type': request.user.user_type,
        }
        return render(request, 'index.html', contexto)
    else:
        return render(request, 'index.html')


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
            return redirect('index')
    else:
        return render(request, 'registrar.html')

