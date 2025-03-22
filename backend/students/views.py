from django.shortcuts import render, redirect
from .models import Student, Group
from django.http import HttpResponse


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
        if request.user.is_authenticated:
            return render(request, 'students/registrar_aluno.html')
        else:
            return HttpResponse(status=400)


