# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0004_clanuser_discord_discriminator'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointsinfo',
            name='elo',
            field=models.PositiveIntegerField(default=1000),
        ),
    ]