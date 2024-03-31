from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import *
class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat')
    search_fields = ('title', 'cat')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'id')


admin.site.register(Doctors, DoctorsAdmin)

admin.site.register(Category, CategoryAdmin)

CustomUser = get_user_model()

admin.site.register(CustomUser)