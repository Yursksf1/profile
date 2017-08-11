from django.contrib import admin

from .models import UserProfile
# Register your models here.



class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'numDoc', 'firsrtName', 'lastName', 'municipality', 'address')
	search_fields = ['user', 'numDoc', 'firsrtName', 'lastName', 'municipality', 'address']

admin.site.register(UserProfile,UserProfileAdmin)



