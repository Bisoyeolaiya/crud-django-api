from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import Student
from .serializers import studentSerializer


class studentList(APIView):

    def get(self, request):
        mystudent = Student.objects.all()
        serializer = studentSerializer(mystudent, many=True)
        return Response(serializer.data)


    def post(self):
        pass