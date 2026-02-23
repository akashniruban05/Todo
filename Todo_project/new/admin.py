from django.contrib import admin
from . models import  Task
# Register your models here.


class admin_config(admin.ModelAdmin):
    list_display = (  'Task' ,  'Is_finished' ,  'updated_at')
    search_fields = ( 'Task', )

admin.site.register (Task,admin_config)