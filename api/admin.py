from django.contrib import admin
from .models import Student, Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'grade', 'gender', 'age')
    list_filter = ('gender', 'grade')
    search_fields = ('student_id', 'first_name', 'last_name')
    ordering = ('student_id',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'first_name', 'last_name', 'subject', 'qualification', 'experience_years')
    list_filter = ('gender', 'subject', 'qualification')
    search_fields = ('teacher_id', 'first_name', 'last_name', 'email')
    ordering = ('teacher_id',)
