from django.contrib import admin
from .models import Roomie

# Register your models here.

@admin.register(Roomie)
class RoomieAdmin(admin.ModelAdmin):
    readonly_fields = ("updated_at",)