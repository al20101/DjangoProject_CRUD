# Generated by Django 3.2.5 on 2022-05-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='study_year',
            field=models.IntegerField(default=2022),
        ),
    ]
