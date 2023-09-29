from django.contrib import admin
from .models import members

class admin_member(admin.ModelAdmin):
    list_display = ['FirstName','LastName','DOB','Email']


admin.site.register(members,admin_member)

