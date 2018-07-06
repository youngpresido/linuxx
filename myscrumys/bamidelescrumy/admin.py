from django.contrib import admin
from .models import ScrumyUser,GoalStatus,ScrumyGoals
# Register your models here.
from django.contrib.auth.models import Group
from .forms import UserAdminCreationForm, UserAdminChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

# User=get_user_model()
# admin.site.register(User)
class UserAdmin(BaseUserAdmin):
	form=UserAdminChangeForm
	add_form=UserAdminCreationForm


	list_display=('email', 'admin')
	list_filter=('admin',)
	fieldsets=(
		(None,{'fields':('username', 'password')}),
		('Personal info',{'fields':()}),
		('permissions',{'fields': ('admin',)}),
		)
	add_fieldsets=(
		(None,{
			'classes':('wide',),
			'fields':('username','password','password2')}
		),
		)
	search_fields=('username',)
	ordering=('username',)
	filter_horizontal=()
admin.site.register(ScrumyUser,UserAdmin)
admin.site.register(ScrumyGoals)
admin.site.register(GoalStatus)
# admin.site.register(ScrumyUser)