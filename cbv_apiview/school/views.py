from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        python_data = request.data
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk=None, format=None):
        id = request.data.get("id")
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None, format=None):
        id = request.data.get("id")
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None, format=None):
        id = request.data.get("id")
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg": "Data Deleted"})
