# Generated by Django 3.2.9 on 2021-11-06 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacunatorios', '0006_rename_abierta_sede_habilitada'),
    ]

    operations = [
        migrations.AddField(
            model_name='sede',
            name='hora_fin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sede',
            name='hora_inicio',
            field=models.IntegerField(default=0),
        ),
    ]
