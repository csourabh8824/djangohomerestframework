from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

# Create your views here.

# Mixins in GenericApi views:
# 1) ListModelMixin: Provides a .list(request, *args, **kwargs) method, that implements listing a queryset.
# 2) CreateModelMixin :Provides a .create(request, *args, **kwargs) method, that implements creating and saving a new model instance.
# 3) RetrieveModelMixin:Provides a .retrieve(request, *args, **kwargs) method, that implements returning an existing model instance in a response.
# 4) UpdateModelMixin: Provides a .update(request, *args, **kwargs) method, that implements updating and saving an existing model instance.
# 5) DestroyModelMixin: Provides a .destroy(request, *args, **kwargs) method, that implements deletion of an existing model instance.


class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()  # Attribute name should be queryset only.
    serializer_class = StudentSerializer
    # Attribute name should be serializer_class only.

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        # list method is present in ListModelMixin that helps to list the queryset


class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        # create method is present in CreateModelMixin to create and save the data


class StudentRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        # retrieve method is present in RetrieveModelMixin to retrieve the data


class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        # update method is present in UpdateModelMixin to update and save the data


class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        # destroy method is present in DestroyModelMixin to destroy or delete the data in database.
