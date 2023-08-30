from django.contrib import admin
from . models import User,Profile


# custom admins

class UserAdmin(admin.ModelAdmin):
    search_fields  = ['full_name', 'username', 'email',  'phone']
    list_display  = ['full_name', 'username', 'email',  'phone']

class ProfileAdmin(admin.ModelAdmin):
    search_fields  = ['user', 'shop_name']
    list_display = ['thumbnail', 'user', 'full_name', 'verified']



# Register your models here.
admin.site.register(User)
admin.site.register(Profile)