from django.contrib import admin

# Importar las clases del modelo
from futbolec.models import EquipoFut, Jugador, Campeonato, CampeonatoEquip
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Se crea la clase heredada de ModelResource
# con el objetivo hacer exclude  para la importación
"""""
class EstudianteResource(resources.ModelResource):
    class Meta:
        model = Estudiante
        exclude = ('modulos', )
"""
# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class EquipoFutAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    

    list_display = ('id','nombre', 'siglas', 'usernameTw')
    search_fields = ('nombre', 'siglas',)
    

# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase EstudianteAdmin
admin.site.register(EquipoFut, EquipoFutAdmin)



# admin.site.register(Matricula)
class JugadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ('nombre', 'posicion', 'numeroCam', 'sueldo')
    search_fields = ('nombre', 'numeroCam',)

admin.site.register(Jugador, JugadorAdmin)
class CampeonatoAdmin (ImportExportModelAdmin, admin.ModelAdmin):

    list_display = ('nombreC', 'nombreAus')
    search_fields = ('nombreC',)

admin.site.register(Campeonato, CampeonatoAdmin)

class CampeonatoEquipAdmin (ImportExportModelAdmin, admin.ModelAdmin):
    list_display= ('equipo', 'campeonato', 'anio')
    search_fields = ('equipo',)

admin.site.register(CampeonatoEquip, CampeonatoEquipAdmin)
