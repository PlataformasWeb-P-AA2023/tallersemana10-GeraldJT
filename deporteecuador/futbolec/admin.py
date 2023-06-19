from django.contrib import admin

# Importar las clases del modelo
from futbolec.models import EquipoFut, Jugador, Campeonato, CampeonatoEquip
# from import_export.admin import ImportExportModelAdmin
# from import_export import resources

# Se crea la clase heredada de ModelResource
# con el objetivo hacer exclude  para la importación
"""
class EstudianteResource(resources.ModelResource):
    class Meta:
        model = Estudiante
        exclude = ('modulos', )
"""
# Se crea una clase que hereda
# de ModelAdmin para el modelo
class EquipoFutAdmin(admin.ModelAdmin):
    

    list_display = ('id','nombre', 'siglas', 'usernameTw')
    search_fields = ('nombre', 'siglas',)
    


admin.site.register(EquipoFut, EquipoFutAdmin)




class JugadorAdmin( admin.ModelAdmin):
  
    list_display = ('nombre', 'posicion', 'numeroCam', 'sueldo')
    search_fields = ('nombre', 'numeroCam',)

admin.site.register(Jugador, JugadorAdmin)
class CampeonatoAdmin ( admin.ModelAdmin):

    list_display = ('nombreC', 'nombreAus')
    search_fields = ('nombreC',)

admin.site.register(Campeonato, CampeonatoAdmin)

class CampeonatoEquipAdmin ( admin.ModelAdmin):
    list_display= ('equipo', 'campeonato', 'anio')
    search_fields = ('equipo',)

admin.site.register(CampeonatoEquip, CampeonatoEquipAdmin)
