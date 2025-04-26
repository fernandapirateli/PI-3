from django.shortcuts import render, redirect
from .models import Student, Group
from users.views import gerir_contexto


def registrar_turma(group_name):
    """
    Cria ou recupera uma turma (Group) com base no nome fornecido.
    Verifica se a turma já existe no banco de dados antes de criar uma nova.
    Caso exista, recupera a turma existente; caso contrário, cria e salva uma nova.

    Args:
        group_name (str): Nome da turma a ser registrada ou recuperada.
    Returns:
        Group: Objeto Group correspondente à turma (nova ou existente).
    """

    if Group.objects.filter(group_name=group_name).exists():
        print('Turma já existente')
        group = Group.objects.get(group_name=group_name)
    else:
        group = Group.objects.create(
            group_name=group_name
        )
        group.save()
    return group


def salvar_aluno(request):
    """
    Processa o cadastro ou edição de um aluno com base nos dados do formulário.
    Para a opção 'registrar_salvar':
    - Verifica se o RA já está cadastrado
    - Cria um novo aluno e sua turma (se necessário)
    - Retorna o nome do aluno e turma em caso de sucesso
    Para a opção 'editar_salvar':
    - Atualiza os dados do aluno existente (incluindo turma)
    - Retorna o nome do aluno e turma atualizados

    Args:
        request (HttpRequest): Objeto de requisição contendo:
            - student_name: Nome completo do aluno
            - student_ra: Registro Acadêmico (RA) do aluno
            - student_diet_restriction: Restrições alimentares
            - group_name: Nome da turma do aluno
            - option: Tipo de operação ('registrar_salvar' ou 'editar_salvar')
            - student_id: ID do aluno (apenas para edição)
    Returns:
        tuple: (nome_do_aluno, nome_da_turma) em caso de sucesso
        HttpResponseRedirect: Redireciona para 'registrar_aluno' se RA já existir
    """

    student_name = request.POST.get('student_name')
    student_ra = request.POST.get('student_ra')
    student_diet_restriction = request.POST.get('student_diet_restriction')
    group_name = request.POST.get('group_name')
    option = request.POST.get('option')

    if option == 'registrar_salvar':
        if Student.objects.filter(student_ra=student_ra).exists():
            print('RA informado já está em uso')
            return redirect('registrar_aluno')

        else:
            group = registrar_turma(group_name)
            student = Student.objects.create(
                student_name=student_name,
                student_ra=student_ra,
                student_diet_restriction=student_diet_restriction,
                student_group=group
            )
            student.save()
            return student.student_name, group_name

    if option == 'editar_salvar':
        student_id = request.POST.get('student_id')
        if Student.objects.filter(pk=student_id).exists():
            student = Student.objects.get(pk=student_id)
            group = registrar_turma(group_name)
            student.student_group = group
            student.student_ra = student_ra
            student.student_name = student_name
            student.student_diet_restriction = student_diet_restriction
            student.save()
            return student.student_name, group_name


def registrar_aluno(request):
    """
    Controla o fluxo de registro de alunos, tratando tanto requisições GET quanto POST.
    Para POST:
    - Chama a função salvar_aluno para processar os dados
    - Redireciona para o perfil após cadastro bem-sucedido
    Para GET:
    - Verifica se o usuário está logado
    - Exibe o formulário de registro ou redireciona para index

    Args:
        request (HttpRequest): Objeto de requisição contendo:
            - POST: Dados do formulário de aluno
            - GET: Nenhum dado específico
    Returns:
        HttpResponseRedirect: Para 'perfil' (sucesso) ou 'index' (não logado)
        HttpResponse: Renderiza formulário de registro para usuários autenticados
    """

    if request.method == 'POST':
        student_name, group_name = salvar_aluno(request)
        if student_name is not None:
            print(f'Aluno(a) {student_name} cadastrado(a) com sucesso na turma {group_name}')
            return redirect('perfil')

    else:
        contexto = gerir_contexto(request)
        if contexto['login']:
            return render(request, 'students/registrar_aluno.html', contexto)

        else:
            return redirect('index')


def listar_alunos(request):
    """
    Exibe a lista de alunos com opção de busca, para usuários autenticados.
    Funcionalidades:
    Exibe todos os alunos ordenados alfabeticamente por nome
    Quando o termo de busca contém apenas letras (isalpha())
    Quando o termo de busca contém números ou números e letras (isalnum())

    Args:
        request (HttpRequest): Objeto de requisição Django contendo:
            - Método POST com parâmetro 'search' (opcional)
            - Sessão do usuário para verificação de autenticação

    Returns:
        HttpResponse: Renderiza 'students/listar_alunos.html' com:
            - Lista completa de alunos (ordem alfabética) OU
            - Resultados filtrados por RA (ordem alfabética)
            - Contexto com informações de login
        HttpResponseRedirect: Redireciona para 'index' se usuário não autenticado
    """

    contexto = gerir_contexto(request)
    lista_alunos = []

    if request.method == 'POST' and contexto['login']:
        search = request.POST.get('search')

        if search.isalpha():
            lista_alunos = Student.objects.order_by('student_name').filter(student_name__icontains=search)
        elif search.isalnum():
            lista_alunos = Student.objects.order_by('student_name').filter(student_ra__icontains=search)
    else:
        if contexto['login']:
            lista_alunos = Student.objects.order_by('student_name').all()
        else:
            return redirect('index')

    contexto['lista_alunos'] = lista_alunos
    return render(request, 'students/listar_alunos.html', contexto)


def perfil_aluno(request):
    """
    Exibe o perfil de um aluno específico quando acessado via POST.
    Recupera os dados do aluno com base no ID fornecido e renderiza a página
    de perfil com essas informações. Acesso restrito via método POST.

    Args:
        request (HttpRequest): Objeto de requisição contendo:
            - POST: student_id (ID do aluno a ser visualizado)
    Returns:
        HttpResponse: Renderiza 'students/perfil_aluno.html' com os dados do aluno
        HttpResponseRedirect: Redireciona para 'index' se acessado via GET
    """

    if request.method == 'POST':
        contexto = gerir_contexto(request)
        student_id = request.POST.get('student_id')
        contexto['student'] = Student.objects.get(pk=student_id)
        return render(request, 'students/perfil_aluno.html', contexto)

    else:
        return redirect('index')


def gerir_aluno(request):
    """
    Gerencia operações CRUD para alunos com base na opção selecionada.
    Trata diferentes ações via POST:
    - 'editar': Prepara formulário de edição com dados do aluno
    - 'editar_salvar': Salva alterações do aluno editado
    - 'excluir': Remove aluno do sistema
    - 'cancelar': Aborta operação atual

    Args:
        request (HttpRequest): Objeto de requisição contendo:
            - option: Ação a ser executada ('editar', 'editar_salvar', 'excluir', 'cancelar')
            - student_id: ID do aluno (para edição/exclusão)
            - Demais campos do formulário (para editar_salvar)
    Returns:
        HttpResponse: Renderiza template de edição (para opção 'editar')
        HttpResponseRedirect: Redireciona para listar_alunos após outras operações
    """

    if request.method == 'POST':
        contexto = gerir_contexto(request)
        option = request.POST.get('option')
        student_id = request.POST.get('student_id')
        if option == 'editar':
            contexto['student'] = Student.objects.get(pk=student_id)
            return render(request, 'students/editar_aluno.html', contexto)

        if option == 'editar_salvar':
            student_name, group_name = salvar_aluno(request)
            print(f'Perfil do aluno(a) {student_name}, da turma {group_name}, foi atualizado com sucesso.')
            return redirect('listar_alunos')

        if option == 'excluir':
            excluir_aluno(student_id)
            return redirect('listar_alunos')

        if option == 'cancelar':
            return redirect('listar_alunos')


def excluir_aluno(student_id):
    """
    Remove permanentemente um aluno do banco de dados com base no ID fornecido.
    Verifica a existência do aluno antes da exclusão e registra a operação
    com os dados do aluno excluído (nome e turma).

    Args:
        student_id (int): ID do aluno a ser excluído.
    """

    if Student.objects.filter(pk=student_id).exists():
        student = Student.objects.get(pk=student_id)
        name, group = student.student_name, student.student_group
        student.delete()
        print(f'O registro do(a) aluno(a) {name}, da turma {group} foi excluído com sucesso')



