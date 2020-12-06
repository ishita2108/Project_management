# Generated by Django 3.1 on 2020-12-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201206_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Web Application', 'Web Application'), ('Desktop Application', 'Desktop Application'), ('Console Application', 'Console Application')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]