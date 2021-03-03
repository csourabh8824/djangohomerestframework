from django.shortcuts import render, HttpResponse
from django.views import View
from django.views.generic import UpdateView, DeleteView
from .forms import RegistrationForm
from .models import Student
# Create your views here.


class Myview(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        students = Student.objects.all()
        return render(request, "school/home.html", context={"form": form, "students": students})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            student_data = Student(name=name, email=email)
            student_data.save()
            return HttpResponse("<h1>Posted</h1>")
        return render(request, "school/home.html", context={"form": form})

    def delete(self, request, id, *args, **kwargs):
        student_data = Student.objects.get(pk=id)
        student_data.delete()
        return HttpResponse("<h1>Deleted!!</h1>")


class StudentUpdateView(UpdateView):
    model = Student
    fields = ["name", "email"]
    success_url = '/thanks/'
    template_name = "school/update.html"


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/thanks/'
    template_name = "school/home.html"
