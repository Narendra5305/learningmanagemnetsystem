from django.contrib import admin

# Register your models here.
from .models import instructorModel,studentModel,Course,Assignment,Solution

admin.site.register(instructorModel)
admin.site.register(studentModel)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Solution)
