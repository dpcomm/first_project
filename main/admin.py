from django.contrib import admin

from .models import Survey_answer,Survey_question,CustomUser

# # Register your models here.
class SqAdmin(admin.ModelAdmin):
    search_fields = ["subject"] # variable name이 반드시 search_fields가 되어야함

admin.site.register(Survey_question,SqAdmin)



from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()

class MyUserAdmin(UserAdmin):
    model = User
    list_dp = ['username','first_name']
admin.site.register(CustomUser,UserAdmin)

