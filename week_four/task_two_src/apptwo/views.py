from django.shortcuts import render
from rest_framework import viewsets
from .models import Student, Coach, Task
from .serializers import StudentSerializer, CoachSerializer, TaskSerializer



class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoachView(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
