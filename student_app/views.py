from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from rest_framework import status
from .serializers import StudentAllSerializer, StudentSerializer
# Create your views here.

class All_students(APIView):
    def get(self, request):
        students = Student.objects.all()
        serialized_students = StudentAllSerializer(students, many=True)
        return Response(serialized_students.data)
    
class A_student(APIView):
    def get(self, request, id):
        student = get_object_or_404(Student, id = id)
        return Response(StudentAllSerializer(student).data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id): 
        student = get_object_or_404(Student, id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)