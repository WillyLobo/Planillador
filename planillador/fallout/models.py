from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class CharFallout(models.Model):
    RAZA = (
        ("H", "Humano"),
        ("G", "Ghoul"),
        ("S", "Super-Mutante"),
        ("D", "Garra Mortal"),
        ("P", "Perro"),
        ("R", "Robot")
    )
    #Datos Generales
    nombrePersonaje = models.CharField("Nombre del Personaje", max_length=60)
    nombreJugador = models.ForeignKey(User, on_delete=models.CASCADE)
    edadPersonaje = models.IntegerField("Edad", validators=[MinValueValidator(1)])
    generoPersonaje = models.CharField("Género", max_length=15)
    razaPersonaje = models.CharField("Raza", max_length=1, choices=RAZA)
    alturaPersonaje = models.DecimalField("Altura", max_digits=3, decimal_places=2, default=1)
    pesoPersonaje = models.IntegerField("Peso", validators=[MinValueValidator(1)])
    
    #Status
    faccionPersonaje = models.CharField("Faccion/Alianza", max_length=60, blank=True, default="Ninguna")
    nivelPersonaje = models.IntegerField("Nivel", validators=[MinValueValidator(1)])
    experienciaPersonaje = models.IntegerField("Experiencia", validators=[MinValueValidator(0)])
    karmaPersonaje = models.IntegerField("Karma")

    #Stats Principales
    StrStat = models.IntegerField("Fuerza", validators=[MinValueValidator(0)])
    PerStat = models.IntegerField("Percepción", validators=[MinValueValidator(0)])
    ResStat = models.IntegerField("Resistencia", validators=[MinValueValidator(0)])
    CarStat = models.IntegerField("Carisma", validators=[MinValueValidator(0)])
    IntStat = models.IntegerField("Inteligencia", validators=[MinValueValidator(0)])
    AgiStat = models.IntegerField("Agilidad", validators=[MinValueValidator(0)])
    SueStat = models.IntegerField("Suerte", validators=[MinValueValidator(0)])

    #Stats Secundarios
    armasPequenasSkill = models.IntegerField("Armas Pequeñas", default=0, validators=[MinValueValidator(0)])
    armasPequenasTag = models.BooleanField("Armas Pequeñas Tag", default=False)

    armasMeleeSkill = models.IntegerField("Armas Melee", default=0, validators=[MinValueValidator(0)])
    armasMeleeTag = models.BooleanField("Armas Melee Tag", default=False)