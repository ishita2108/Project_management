from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Project

# Create your views here.
def home_view(request, *args, **kwargs):
    students = Student.objects.all()
    
    stu = []
    for index, student in enumerate(students):
        stu_dict={}
        stu_dict['index'] = index+1
        stu_dict['student']= student
        proj= student.project.all().first()
        stu_dict['project'] = proj
        stu.append(stu_dict)
    print(stu)
    context = {'students':stu}
    return render(request, 'home.html', context)


def detail_view(request, id, *args, **kwargs):
    student = Student.objects.get(id=id)
    stu_dict = {}
    stu_dict['student'] = student
    proj= student.project.all().first()
    stu_dict['project'] = proj
    context = {'student':stu_dict}
    return render(request, 'stu.html', context)
