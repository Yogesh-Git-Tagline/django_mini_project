from django.contrib import admin
from . models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email_id','contact_number','address','photo']

