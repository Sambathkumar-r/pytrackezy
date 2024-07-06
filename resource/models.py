from django.contrib import admin
from django.db import models


class Resource(models.Model):
    emp_no = models.IntegerField()
    emp_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10,default='Male',
                              choices=[('Male', 'Male'),
                                       ('Female', 'Female')])
    mode_of_employ = models.CharField(max_length=30,default='Employee',
                                      choices=[('Employee', 'Employee'),
                                               ('Consultant', 'Consultant'),
                                               ('Contingent worker', 'Contingent worker'),
                                               ('Business User', 'Business User')])
    employee_type = models.CharField(max_length=30,default='Employee',
                                      choices=[('Employee', 'Employee'),
                                               ('Contractor', 'Contractor'),
                                               ('Global Employee', 'Global Employee')])
    designation = models.CharField(max_length=30)
    emp_grade = models.CharField(max_length=2)
    practice = models.CharField(max_length=40,default='Dotnet',
                                      choices=[('Dotnet', 'Dotnet'),
                                               ('Solutioning', 'Solutioning'),
                                               ('Quality Assurance', 'Quality Assurance'),
                                               ('Delivery Excellence', 'Delivery Excellence')])
    emp_role = models.CharField(max_length=40)
    doj = models.DateField()
    dol = models.DateField(null=True,blank=True)
    Location = models.CharField(max_length=15)

    countryChoices = (
        ('IN','India'),
        ('US','United states'),
        ('CA','Canada'),
        ('MX','Mexico'),
        ('OT','Others')
    )

    Country = models.CharField(max_length=20,default='IN',choices=countryChoices)
    emp_status = models.CharField(max_length=10,default='Active',
                              choices=[('Active', 'Active'),
                                       ('Inactive', 'Inactive'),
                                       ('Resigned', 'Resigned')])

    image_url = models.CharField(max_length=2083)


class Projects(models.Model):
    pid_no = models.IntegerField()
    project_name = models.CharField(max_length=30)
    business_unit = models.CharField(max_length=15)
    vertical = models.CharField(max_length=15)
    Customer_id = models.IntegerField()
    Market = models.CharField(max_length=15)
    start_date = models.DateField()
    end_date = models.DateField()
    project_type = models.CharField(max_length=20)
    execution_type = models.CharField(max_length=20)
    prj_plan_mandays = models.FloatField()
    prd_plan_mandays = models.FloatField()
    pm_name = models.CharField(max_length=30)
    revenue_local_currency = models.FloatField()


