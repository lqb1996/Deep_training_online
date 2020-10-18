from django.contrib import admin

from .models import *


@admin.register(Aisline)
class AislineAdmin(admin.ModelAdmin):
    list_display = ()
    fields = ()


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ()
    fields = ()
