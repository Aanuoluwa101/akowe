from django.contrib import admin
from .models import Officiator

# Register your models here.
@admin.register(Officiator)
class OfficiatorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Officiator._meta.fields]
    list_filter = ['id']