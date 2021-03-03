from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import RegistrationForm
from .models import Student
# Create your viewsfrom .models import Student here.


class StudentCreateView(CreateView):
    form_class = RegistrationForm
    # fields = ["name", "email"]
    template_name = "student/home.html"
    success_url = "/thanks/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student"] = Student.objects.all()
        return context


class StudentUpdateView(UpdateView):
    model = Student
    fields = ["name", "email"]
    template_name = "student/update.html"
    success_url = "/thanks/"


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student/delete.html"
    success_url = "/thanks/"
