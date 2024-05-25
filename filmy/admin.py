from django.contrib import admin
from filmy.models import Movie, Director, Genre, Actor, Fotbal

class MovieAdmin(admin.ModelAdmin):
    pass


class DirectorAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass

class ActorAdmin(admin.ModelAdmin):
    pass

class FotbalAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)

admin.site.register(Director, DirectorAdmin)

admin.site.register(Genre, GenreAdmin)

admin.site.register(Actor, ActorAdmin)

admin.site.register(Fotbal, FotbalAdmin)