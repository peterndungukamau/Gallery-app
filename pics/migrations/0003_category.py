# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-12-14 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0002_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=60)),
                ('post', models.TextField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pics.Image')),
                ('location', models.ManyToManyField(to='pics.location')),
            ],
        ),
    ]
