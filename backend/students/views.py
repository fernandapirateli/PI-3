from django.shortcuts import render, redirect
from .models import Student, Group
from users.views import gerir_contexto


def registrar_turma(group_name):
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
            return redirect('index', contexto)


def listar_alunos(request):
    contexto = gerir_contexto(request)
    if request.method == 'POST':
        pass
    else:
        if contexto['login']:
            lista_alunos = Student.objects.order_by('student_name').all()
            contexto['lista_alunos'] = lista_alunos
            return render(request, 'students/listar_alunos.html', contexto)

        else:
            return redirect('index')


def perfil_aluno(request):
    if request.method == 'POST':
        contexto = gerir_contexto(request)
        student_id = request.POST.get('student_id')
        contexto['student'] = Student.objects.get(pk=student_id)
        return render(request, 'students/perfil_aluno.html', contexto)

    else:
        return redirect('index')


def editar_aluno(request):
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
            pass
