from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Habit)
admin.site.register(TaskTracker)
admin.site.register(Streak)
admin.site.register(Achievement)