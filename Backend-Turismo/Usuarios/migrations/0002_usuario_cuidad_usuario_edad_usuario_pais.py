# Generated by Django 4.1.1 on 2022-09-29 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cuidad',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ciudad'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='edad',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Edad'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pais',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Pais'),
        ),
    ]
