from django.contrib import admin
from .models import ScrumyUser,GoalStatus,ScrumyGoals
# Register your models here.

admin.site.register(ScrumyGoals)
admin.site.register(GoalStatus)
admin.site.register(ScrumyUser)