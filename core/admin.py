from django.contrib import admin
from core.models import Evento


# Configuração do display do admin do Django (essa config se sobrepõe àquela feita no models -> [def __str__])
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ['usuario', 'data_evento']


admin.site.register(Evento, EventoAdmin)
