from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from CustomAdminPanel.models import CustomUser, Doctors, Departments, Service


# Register your models here.
class UserModel(UserAdmin):
    pass


admin.site.register(CustomUser, UserModel)
admin.site.register(Doctors)
admin.site.register(Departments)
admin.site.register(Service)

