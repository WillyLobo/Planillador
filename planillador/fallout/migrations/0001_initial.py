# Generated by Django 4.1.3 on 2022-12-12 21:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CharFallout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePersonaje', models.CharField(max_length=60, verbose_name='Nombre del Personaje')),
                ('edadPersonaje', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Edad')),
                ('generoPersonaje', models.CharField(max_length=15, verbose_name='Género')),
                ('razaPersonaje', models.CharField(choices=[('H', 'Humano'), ('G', 'Ghoul'), ('S', 'Super-Mutante'), ('D', 'Garra Mortal'), ('P', 'Perro'), ('R', 'Robot')], max_length=1, verbose_name='Raza')),
                ('alturaPersonaje', models.DecimalField(decimal_places=2, default=1, max_digits=3, verbose_name='Altura')),
                ('pesoPersonaje', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Peso')),
                ('faccionPersonaje', models.CharField(blank=True, default='Ninguna', max_length=60, verbose_name='Faccion/Alianza')),
                ('nivelPersonaje', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Nivel')),
                ('experienciaPersonaje', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Experiencia')),
                ('karmaPersonaje', models.IntegerField(verbose_name='Karma')),
                ('StrStat', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Fuerza')),
                ('PerStat', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Percepción')),
                ('ResStat', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Resistencia')),
                ('CarStat', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Carisma')),
                ('IntStat', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Inteligencia')),
                ('AgiStat', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Agilidad')),
                ('SueStat', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Suerte')),
                ('armasPequenasSkill', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Armas Pequeñas')),
                ('armasPequenasTag', models.BooleanField(default=False, verbose_name='Armas Pequeñas Tag')),
                ('nombreJugador', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
