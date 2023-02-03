from django.contrib import admin

from StudentApp.models import City, Course, Student

# Register your models here.
admin.site.register(City)
admin.site.register(Course)
admin.site.register(Student)