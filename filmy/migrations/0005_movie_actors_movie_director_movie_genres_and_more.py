# Generated by Django 5.0.3 on 2024-05-31 06:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0004_fotbal'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, to='filmy.actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='filmy.director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, to='filmy.genre'),
        ),
        migrations.AlterField(
            model_name='director',
            name='main_picture',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]