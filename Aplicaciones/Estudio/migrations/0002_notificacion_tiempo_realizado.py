# Generated by Django 4.0.6 on 2024-12-28 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='tiempo_realizado',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
