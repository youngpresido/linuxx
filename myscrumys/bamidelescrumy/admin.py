from django.contrib import admin
from .models import ScrumyUser,GoalStatus,ScrumyGoals
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

# User=get_user_model()
# admin.site.register(User)
admin.site.register(ScrumyUser)
admin.site.register(ScrumyGoals)
admin.site.register(GoalStatus)
# admin.site.register(ScrumyUser)