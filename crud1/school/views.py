from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from .models import Student
# Create your views here.


def home(request):
    students = Student.objects.all()
    return render(request, "school/home.html", context={"students": students})


def add_student(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            student_data = Student(
                name=form.cleaned_data['name'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            student_data.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, "school/register.html", context={"form": form})


def update_student(request, id):
    student_data = Student.objects.get(pk=id)
    if request.method == "POST":
        form = RegisterForm(request.POST, instance=student_data)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterForm(instance=student_data)
    return render(request, "school/update.html", context={"form": form})


def delete_data(request, id):
    student_data = Student.objects.get(pk=id)
    student_data.delete()
    return HttpResponse("<h1>DATA DELETED</h1>")
