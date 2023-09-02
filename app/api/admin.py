from django.contrib import admin

from api.models import User, Cat, Dog


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'age')


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'age')
