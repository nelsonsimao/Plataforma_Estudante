from django.contrib import admin
from alojamentos.models import AlugoCasa

#isto cria uma especie de view so que eu quero
#class AnuncioAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'titulo']


admin.site.register(AlugoCasa)
#admin.site.register(Anuncio, AnuncioAdmin)

