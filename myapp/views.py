from django.shortcuts import render
from .models import Students

def index(request):
    student = Students.objects.get(pk=1)
    return render(request,'myapp/index.html',{'stu':student,'num':10})

def students(request):
    stulist = Students.objects.all()
    return render(request,'myapp/students.html',{'students':stulist})