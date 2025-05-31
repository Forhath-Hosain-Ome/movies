from django.contrib import admin

from .models import *

# Register your models here.

# admin.site.register(Movies)
# admin.site.register(Director)
# admin.site.register(CoDirector)
# admin.site.register(Actor)

@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'is_available', 'genra', 'direct')  # show these columns in list
    list_filter = ('release_year', 'genra', 'is_available')  # add sidebar filters
    search_fields = ('title', 'description')  # add search bar
    ordering = ('-release_year',)
    filter_horizontal = ('actors', 'codir')  # better many-to-many field UI
    autocomplete_fields = ('direct',)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(CoDirector)
class CoDirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
