import io
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Student
# Create your views here.


@csrf_exempt
def student_api(request, id):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id", None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {"msg": "Data Created!"}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

    if request.method == "PUT":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data)
        if serializer.is_valid():
            serializer.save()
            response = {"msg": "Data Updated!!"}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type="application/json")
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type="application/json")

    if request.method == "DELETE":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        stu = Student.objects.get(id=id)
        stu.delete()
        response = {"msg": "Data Deleted!!"}
        json_data = JSONRenderer().render(response)
        return HttpResponse(json_data, content_type="application/json")
