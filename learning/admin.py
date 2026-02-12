from django.contrib import admin
from learning.models import Profile

# Register your models here.
@admin.register(Profile)
class ProdileAdmin(admin.ModelAdmin):
    list_display = ['user', 'notifications']
