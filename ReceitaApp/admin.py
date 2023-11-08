from django.contrib import admin
from ReceitaApp.models import Categoria, Receita
# Register your models here.

class ReceitaAdmin(admin.ModelAdmin):
    list_display = [ 'nome', 'grau_de_dificuldade', 'categoria']
    list_filter = ['grau_de_dificuldade', 'categoria' ]
    list_display_links = ['nome']   
    search_fields = ['nome']
    
admin.site.register(Categoria)
admin.site.register(Receita, ReceitaAdmin)