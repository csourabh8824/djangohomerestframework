from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
# Create your views here.
# request.data contains all the data i.e id,name,roll,city It has a data parsed in python
# We don't have to use JSONParser() to convert in python


# Response(data, status=None, template_name=None, headers=None, content_type=None)

#     data: The serialized data for the response.(python data)
#     status: A status code for the response. Defaults to 200. See also status codes.
#     template_name: A template name to use if HTMLRenderer is selected.
#     headers: A dictionary of HTTP headers to use in the response.
#     content_type: The content type of the response. Typically, this will be set automatically by the renderer as determined by content negotiation, but there may be some cases where you need to specify the content type explicitly.


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def student_api(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        python_data = request.data
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "data updated"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    if request.method == "PATCH":
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Updated Partially"})
        return Response(serializer.errors)

    if request.method == "DELETE":
        id = request.data.get("id")
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({"msg": "Data Deleted"})
