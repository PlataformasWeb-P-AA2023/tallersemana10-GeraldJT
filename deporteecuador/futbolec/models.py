from django.db import models

# Create your models here.

class EquipoFut(models.Model):

    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30) # Verbose field names
    usernameTw = models.CharField(max_length=30)

    campeonatoEquip = models.ManyToManyField('Campeonato', through='CampeonatoEquip')


    def __str__(self):
        return "%s - %s - %s:" % (self.nombre,
                self.siglas,
                self.usernameTw)


class Jugador(models.Model):
    """
    """
    nombre = models.CharField(max_length=30)
    posicion = models.CharField(max_length=30)
    numeroCam = models.IntegerField()
    sueldo = models.IntegerField()
    equipo = models.ForeignKey(EquipoFut, on_delete=models.CASCADE, \
            related_name="losjugadores")


    def __str__(self):
        return "%s - %s - %s - %s - %s:" % (self.nombre,
                self.posicion,
                self.numeroCam,
                self.sueldo,
                self.equipo)

class Campeonato(models.Model):

    nombreC = models.CharField(max_length=50)
    nombreAus = models.CharField(max_length=50)
    campeonatoequip = models.ManyToManyField('EquipoFut', through= 'CampeonatoEquip')
    
    def __str__(self):
        return "%s - %s:" % (self.nombreC,
                self.nombreAus,
                self.campeonatoequip)

class CampeonatoEquip(models.Model):
    
    
    equipo = models.ForeignKey(EquipoFut, related_name='losequipos',
            on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, related_name='losequipos',
            on_delete=models.CASCADE)
    anio = models.IntegerField()

    def __str__(self):
        return "%s - %s - %d" % \
                (self.equipo, self.campeonato, self.anio)
