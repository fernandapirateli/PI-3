from django.shortcuts import render, redirect
from .models import Student, Group


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


def registrar_aluno(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_ra = request.POST.get('student_ra')
        student_diet_restriction = request.POST.get('student_diet_restriction')
        group_name = request.POST.get('group_name')

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
            print(f'Aluno(a) {student_name} cadastrado(a) com sucesso na turma {group.group_name}')
            return redirect('perfil')
    else:
        contexto = {'login': False}
        if request.user.is_authenticated:
            if request.user.is_authenticated:
                contexto = {
                    'first_name': request.user.first_name,
                    'user_type': request.user.user_type,
                    'login': True,
                }
            return render(request, 'students/registrar_aluno.html', contexto)
        else:
            return redirect('index', contexto)


