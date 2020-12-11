from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings
from .models import Student, Project
from .forms import StudentForm, ProjectForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    students = Student.objects.all()
    
    stu = []
    for index, student in enumerate(students):
        stu_dict={}
        stu_dict['index'] = index+1
        stu_dict['student']= student
        proj= student.project
        stu_dict['project'] = proj
        stu.append(stu_dict)
    context = {'students':stu}
    return render(request, 'home.html', context)


def detail_view(request, id, *args, **kwargs):
    student = Student.objects.get(id=id)
    stu_dict = {}
    stu_dict['student'] = student
    proj= student.project
    stu_dict['project'] = proj
    context = {'student':stu_dict}
    return render(request, 'stu.html', context)

def search_view(request, *args, **kwargs ):
    students = Student.objects.all() 
    return render(request, 'filter.html')

def create_student(request, *args, **kwargs ):
    print(request.POST.get("name"))
    name = request.POST.get("name")
    branch = request.POST.get("branch")
    enroll = request.POST.get("enroll")
    section = request.POST.get("section")

    project = request.POST.get("project")
    language = request.POST.get("language")
    category = request.POST.get("category")
    description = request.POST.get("description")
    

    # form = StudentForm(request.POST or None)
    # formp = ProjectForm(request.POST or None)
    # print(formp)
    # #next_url = request.POST.get("next") or None
    # if form.is_valid():
    #     print("HELLO")
    #     obj = form.save()
    #     form = StudentForm()
    # if formp.is_valid():
    #     print("HELLO")
    #     obj2 = formp.save()
    #     obj2.save()
    #     print(obj2.id)
    #     proj = Project.objects.get(id=obj2.id)
    #     obj.save(project=proj)
    #     if request.is_ajax():
    #         return JsonResponse(obj.serialize(), status=201)
    #     formp = ProjectForm()
    project_obj = Project(name=project, language=language, category=category, description=description)
    project_obj.save()
    student_obj = Student(name=name, branch=branch,enroll=enroll, section=section, project=project_obj)
    student_obj.save()
    return JsonResponse(student_obj.serialize(), status=201)
