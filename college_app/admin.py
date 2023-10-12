from django.contrib import admin

from college_app.models import Register, Course, Department,Purpose

# Register your models here.

admin.site.register(Register)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Purpose)