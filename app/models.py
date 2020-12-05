from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    language = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
      
    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    project = models.ManyToManyField('Project',null=True, blank=True)
    enroll = models.CharField(max_length=12)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    
    

    