# Generated by Django 4.1 on 2022-09-26 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0015_remove_camionetaimagen_camioneta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camioneta',
            name='imagen',
            field=models.ImageField(null=True, upload_to='camionetas'),
        ),
        migrations.AlterField(
            model_name='moto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='motos'),
        ),
    ]
