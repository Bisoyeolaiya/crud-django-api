from rest_framework import serializers
from .models import Student, Coach, Task


class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coach
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'