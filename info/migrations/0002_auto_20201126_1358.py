# Generated by Django 3.1.2 on 2020-11-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assigntime',
            name='period',
            field=models.CharField(choices=[('8:30 - 9:30', '8:30 - 9:30'), ('9:30 - 10:30', '9:30 - 10:30'), ('11:00 - 11:50', '11:00 - 11:50'), ('11:50 - 12:40', '11:50 - 12:40'), ('12:40 - 1:30', '12:40 - 1:30'), ('2:30 - 3:30', '2:30 - 3:30'), ('3:30 - 4:30', '3:30 - 4:30')], default='11:00 - 11:50', max_length=50),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default='2020-8-01'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=50),
        ),
    ]
