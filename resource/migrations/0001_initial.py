# Generated by Django 5.0.2 on 2024-03-03 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_no', models.IntegerField()),
                ('emp_name', models.CharField(max_length=30)),
                ('emp_class', models.CharField(max_length=2)),
                ('mode_of_employ', models.CharField(max_length=10)),
                ('employee_type', models.CharField(max_length=10)),
                ('designation', models.CharField(max_length=15)),
                ('emp_grade', models.CharField(max_length=2)),
                ('practice', models.CharField(max_length=15)),
                ('emp_role', models.CharField(max_length=25)),
                ('doj', models.DateField()),
                ('Location', models.CharField(max_length=15)),
                ('Country', models.CharField(max_length=15)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
