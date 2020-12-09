from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings
from .models import Student, Project
from .forms import StudentForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

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

def search_view(request, *args, **kwargs ):
    students = Student.objects.all() 
    return render(request, 'filter.html')

def create_student(request, *args, **kwargs ):
    print(request.POST)
    form = StudentForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        print("HELLO")
        obj = form.save()
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        form = StudentForm()
    return render(request, 'form.html', context={"form":form})
