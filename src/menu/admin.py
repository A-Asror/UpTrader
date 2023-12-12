from django.contrib import admin
from .models import MenuModel


class MenuModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent')


admin.site.register(MenuModel, MenuModelAdmin)
