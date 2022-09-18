# Generated by Django 4.1 on 2022-09-17 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, unique=True)),
                ('subtitulo', models.CharField(max_length=50)),
                ('cuerpo', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Camioneta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, unique=True)),
                ('subtitulo', models.CharField(max_length=50)),
                ('cuerpo', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='media')),
            ],
        ),
        migrations.CreateModel(
            name='Moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, unique=True)),
                ('subtitulo', models.CharField(max_length=50)),
                ('cuerpo', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=20)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(null=True, upload_to='media')),
            ],
        ),
    ]