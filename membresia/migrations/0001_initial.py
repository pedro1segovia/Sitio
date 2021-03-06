# Generated by Django 3.2 on 2022-07-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('contacto', models.IntegerField()),
                ('correo_electronico', models.CharField(max_length=70)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otros')], max_length=3)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_ingreso', models.DateField()),
            ],
        ),
    ]
