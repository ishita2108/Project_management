from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings
from .models import Student, Project

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
    students = Student.objects.all()
    projects = Project.objects.all()
    name = request.GET.get('name')
    project = request.GET.get('project')
    enroll = request.GET.get('enroll')
    section = request.GET.get('section')
    language = request.GET.get('language')
    category = request.GET.get('category')
    
    if name:
        students = students.filter(name__icontains = name)
        print(students)
    if enroll:
        students = students.filter(enroll__icontains = enroll)
        print(students)
    if section:
        students = students.filter(section__icontains = section)
        print(students)
    if project:
        projects = projects.filter(name__icontains=project)
        proj_id_list = []
        for project in projects:
            proj_id_list.append(project.id)
        students = students.filter(project__in = proj_id_list)
        print(students)
    if language:
        projects = projects.filter(language__icontains=language)
        proj_id_list = []
        for project in projects:
            proj_id_list.append(project.id)
        students = students.filter(project__in = proj_id_list)
        print(students)
    if category:
        projects = projects.filter(category__icontains= category)
        proj_id_list = []
        for project in projects:
            proj_id_list.append(project.id)
        students = students.filter(project__in = proj_id_list)
        print(students)

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
    if request.method == "POST":
        name = request.POST.get("name")
        branch = request.POST.get("branch")
        enroll = request.POST.get("enroll")
        section = request.POST.get("section")

        project = request.POST.get("project")
        language = request.POST.get("language")
        category = request.POST.get("category")
        description = request.POST.get("description")
        project_obj = Project(name=project, language=language, category=category, description=description)
        check_enroll = Student.objects.filter(enroll=enroll)
        if check_enroll.exists():
            return JsonResponse({"msg":"Enrollment Number already exists"}, status=400)
        student_obj = Student(name=name, branch=branch,enroll=enroll, section=section, project=project_obj)
        project_obj.save()
        student_obj.save()
        return JsonResponse(student_obj.serialize(), status=201)
    else:
        return JsonResponse({"msg": "Method Not Allowed"})

def delete_student(request, *args, **kwargs):
    if request.method == "POST":
        id = request.POST.get('id')
        try:
            qs = Student.objects.filter(id = id)
        except:
            return JsonResponse({"msg": "Student does not exist."}, status=404)
        if qs.exists():
            obj = qs.first()
            obj.delete()
            return JsonResponse({"msg":"Found"}, status=200)
    else:
        return JsonResponse({"msg": "Method Not Allowed"})

def edit_student(request, *args, **kwargs):
    if request.method == "POST":
        try:
            stu_id = request.POST.get("stu_id")
            proj_id = request.POST.get("proj_id")
        except:
            return JsonResponse({"msg": "Does not exist."}, status=404)
        student = Student.objects.get(id = stu_id)
        project = Project.objects.get(id = proj_id)
        student.name = request.POST.get("name")
        student.enroll = request.POST.get("enroll")
        student.branch = request.POST.get("branch")
        student.section = request.POST.get("section")
        project.name = request.POST.get("project")
        project.language = request.POST.get("language")
        project.category = request.POST.get("category")
        project.description = request.POST.get("description")
        student.save()
        project.save()
        return JsonResponse({'msg': stu_id}, status=201)
    else:
        return JsonResponse({"msg": "Method Not Allowed"})

    