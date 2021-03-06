# Generated by Django 3.1 on 2020-12-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_project_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='doc/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(choices=[('C', 'C'), ('C++', 'C++'), ('Java', 'Java'), ('Python', 'Python')], max_length=20),
        ),
    ]
