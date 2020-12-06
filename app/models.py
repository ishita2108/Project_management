from django.db import models

# Create your models here.
class Project(models.Model):
    TUP = (
        ('Web Application','Web Application'),
        ('Desktop Application', 'Desktop Application'),
        ('Console Application', 'Console Application')
    )
    LANG =(
        ('C','C'),
        ('C++', 'C++'),
        ('Java','Java'),
        ('Python','Python')
    )
    name = models.CharField(max_length=30)
    language = models.CharField(max_length=20,  choices = LANG)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=20, choices = TUP)
    document = models.FileField(upload_to = 'static/doc/' ,null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
      
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    project = models.ManyToManyField('Project',null=True, blank=True)
    enroll = models.CharField(max_length=12)
    branch = models.CharField(max_length=12)
    section = models.CharField(max_length=5)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    
    

    