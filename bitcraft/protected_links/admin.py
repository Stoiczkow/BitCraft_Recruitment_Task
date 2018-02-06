from django.contrib import admin
from .models import Links, Files


# Register your models here.
@admin.register(Links)
class Links(admin.ModelAdmin):
    list_display = ("address", "password")


@admin.register(Files)
class Files(admin.ModelAdmin):
    list_display = ("token", "password")
