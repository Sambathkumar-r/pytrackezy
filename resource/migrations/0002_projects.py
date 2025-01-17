# Generated by Django 5.0.2 on 2024-03-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid_no', models.IntegerField()),
                ('project_name', models.CharField(max_length=30)),
                ('business_unit', models.CharField(max_length=15)),
                ('vertical', models.CharField(max_length=15)),
                ('Customer_id', models.IntegerField()),
                ('Market', models.CharField(max_length=15)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('project_type', models.CharField(max_length=20)),
                ('execution_type', models.CharField(max_length=20)),
                ('prj_plan_mandays', models.FloatField()),
                ('prd_plan_mandays', models.FloatField()),
                ('pm_name', models.CharField(max_length=30)),
                ('revenue_local_currency', models.FloatField()),
            ],
        ),
    ]
