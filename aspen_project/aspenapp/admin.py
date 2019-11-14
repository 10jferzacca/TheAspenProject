from django.contrib import admin
from .models import Adventure
# Register your models here.
class AdventureAdmin(admin.ModelAdmin):  # add this
      list_display = ('title', 'description', 'completed')

admin.site.register(Adventure, AdventureAdmin)