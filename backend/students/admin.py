from django.contrib import admin
from .models import Student, Group


class ListStudents(admin.ModelAdmin):
    list_display = ('student_name', 'student_group')
    list_display_links = ('student_name', 'student_group')
    search_fields = ('student_name',)
    list_per_page = 20


class ListGroups(admin.ModelAdmin):
    list_display = ('group_name',)
    list_display_links = ('group_name',)
    search_fields = ('group_name',)
    list_per_page = 20


admin.site.register(Student, ListStudents)
admin.site.register(Group, ListGroups)
