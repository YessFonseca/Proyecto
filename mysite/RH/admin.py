from django.contrib import admin

from .models import Trabajador,CategoriaDocente,CategoriaCientifica,NivelEscolaridad

admin.site.register(Trabajador)
admin.site.register(NivelEscolaridad)
admin.site.register(CategoriaCientifica)
admin.site.register(CategoriaDocente)



