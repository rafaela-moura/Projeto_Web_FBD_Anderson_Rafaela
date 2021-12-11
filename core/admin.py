from django.contrib import admin
from .models import Filme,Serie,Anime,Genero,Idioma, Agenda


admin.site.register(Filme)
admin.site.register(Serie)
admin.site.register(Anime)
admin.site.register(Genero)
admin.site.register(Idioma)
admin.site.register(Agenda)

# Register your models here.
