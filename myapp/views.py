from django.shortcuts import render
from .models import Students

def index(request):
    student = Students.objects.get(pk=1)
    return render(request,'myapp/index.html',{'stu':student,'num':10,'str':'disman','list':['disman','disman1'],'test':'10'})

def students(request):
    stulist = Students.objects.all()
    return render(request,'myapp/students.html',{'students':stulist})

def good(request,id):
    return render(request,'myapp/good.html',{'num':id})

def main(request):
    return render(request,'myapp/main.html')
def detail(request):
    return render(request,'myapp/detail.html')