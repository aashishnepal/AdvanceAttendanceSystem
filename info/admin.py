from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.student)
admin.site.register(models.attendance_history)
admin.site.register(models.total_record)