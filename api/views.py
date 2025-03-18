from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['gender', 'grade']
    search_fields = ['first_name', 'last_name', 'student_id']
    ordering_fields = ['first_name', 'last_name', 'student_id', 'grade']
    ordering = ['student_id']

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['gender', 'subject', 'qualification']
    search_fields = ['first_name', 'last_name', 'teacher_id', 'email']
    ordering_fields = ['first_name', 'last_name', 'teacher_id', 'subject']
    ordering = ['teacher_id']
