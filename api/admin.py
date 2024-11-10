from django.contrib import admin
from .models import UsersProyect, TypeProject, ProjectData, Users, Address, Finance


# Register your models here.
admin.site.register(Users)
admin.site.register(Address)
admin.site.register(Finance)

admin.site.register(UsersProyect)
admin.site.register(TypeProject)
admin.site.register(ProjectData)
