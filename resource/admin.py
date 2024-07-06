from django.contrib import admin
from .models import Resource,Projects


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('emp_no','emp_name','designation','Location')


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('pid_no','project_name','business_unit','Customer_id','Market')


admin.site.register(Resource,ResourceAdmin)
admin.site.register(Projects,ProjectsAdmin)