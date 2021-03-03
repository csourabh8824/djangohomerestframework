from django.shortcuts import render
from .models import Student
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
# Create your views here.

"""
ViewSet class is a class based view that does not provide any method handlers like get(),post(),put() etc
instead of the method handlers it provides actions such as list(),create,retrieve(),update() etc.
"""

"""
Actions:
 list(): Give all records.
 create(): Creates a record.
 update(): updates record completely.
 partial_update(): updates record partially.
 retrieve(): give single record.
 destroy(): deletes an existing record
"""

"""
Attributes in viewset:
 basename: This is a name defined on URL dispatcher.
 action: the name of current action example list(),create()etc
 detail,suffix,name,description
"""

"""
viewset url config(urls.py):
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router = DefaultRouter() #creating default router object
router.register("studentapi",views)
urlpatterns = [
    path("",include(router.urls)),
]
"""


class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def create(self, request):
        python_data = request.data
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "data created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_200_BAD_REQUEST)

    def update(self, request, pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Complete data updated"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_200_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Partial data updated"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_200_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg": "data deleted"})
