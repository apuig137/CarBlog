# Generated by Django 4.1 on 2022-09-25 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0011_autoimagen_nombre_camionetaimagen_nombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autoimagen',
            old_name='nombre',
            new_name='articulo',
        ),
        migrations.RenameField(
            model_name='autoimagen',
            old_name='auto',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='camionetaimagen',
            old_name='nombre',
            new_name='articulo',
        ),
        migrations.RenameField(
            model_name='camionetaimagen',
            old_name='camioneta',
            new_name='model',
        ),
        migrations.RenameField(
            model_name='motoimagen',
            old_name='nombre',
            new_name='articulo',
        ),
        migrations.RenameField(
            model_name='motoimagen',
            old_name='moto',
            new_name='model',
        ),
    ]