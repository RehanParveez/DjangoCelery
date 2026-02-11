from django.contrib import admin
from fishta.models import Profile

# Register your models here.
@admin.register(Profile)
class ProdileAdmin(admin.ModelAdmin):
    list_display = ['user', 'notifications']
