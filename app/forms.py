from django import forms
from .models import Student, Project

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','enroll','branch','section']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','language','category','description']