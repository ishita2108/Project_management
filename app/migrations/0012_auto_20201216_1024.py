# Generated by Django 3.1 on 2020-12-16 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_project_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enroll',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
