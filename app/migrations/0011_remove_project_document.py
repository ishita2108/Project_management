# Generated by Django 3.1 on 2020-12-16 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20201215_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='document',
        ),
    ]
