from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Hippo


@admin.register(Hippo)
class MovieAdmin(admin.ModelAdmin):
    fields = (
        "name", "color", "age",
    )
    list_display = (
        "name", "color", "age",
    )
