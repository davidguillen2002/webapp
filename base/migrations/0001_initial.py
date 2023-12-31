# Generated by Django 4.2.6 on 2023-10-24 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('calorias', models.DecimalField(decimal_places=2, max_digits=6)),
                ('proteinas', models.DecimalField(decimal_places=2, max_digits=6)),
                ('carbohidratos', models.DecimalField(decimal_places=2, max_digits=6)),
                ('grasas', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='alimentos_imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Nutriente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(choices=[('vitamina', 'Vitamina'), ('mineral', 'Mineral')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroDiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=6)),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.alimento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilNutricional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.PositiveIntegerField()),
                ('sexo', models.CharField(choices=[('Hombre', 'Hombre'), ('Mujer', 'Mujer')], max_length=10)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=6)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=6)),
                ('nivel_actividad', models.CharField(choices=[('sedentario', 'Sedentario'), ('ligero', 'Ligero'), ('moderado', 'Moderado'), ('intenso', 'Intenso'), ('muy_intenso', 'Muy Intenso')], max_length=50)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AlimentoNutriente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=6)),
                ('unidad', models.CharField(max_length=20)),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.alimento')),
                ('nutriente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.nutriente')),
            ],
        ),
        migrations.AddField(
            model_name='alimento',
            name='nutrientes',
            field=models.ManyToManyField(through='base.AlimentoNutriente', to='base.nutriente'),
        ),
        migrations.AddField(
            model_name='alimento',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
