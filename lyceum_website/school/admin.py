from django.contrib import admin
from .models import School

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time', 'is_publised')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_publised',)
    list_filter = ('is_publised', 'time')

admin.site.register(School, SchoolAdmin)