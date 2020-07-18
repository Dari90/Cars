from django.contrib import admin
from app.models import Cars

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    pass
