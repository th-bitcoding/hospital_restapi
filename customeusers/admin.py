from django.contrib import admin
from customeusers.models import CustomeUser

@admin.register(CustomeUser)
class CustomeUserAdmin(admin.ModelAdmin):
    list_display = ['id','username','phone_number','email','gender','address','date_of_birth']
